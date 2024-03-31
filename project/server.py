from flask import Flask, render_template, request, redirect
from lib_iron.class_sort_iron import dict_word
from data import db_session
from data.word import Word

app = Flask(__name__)

attemps = 7
count_of_words_entered = 0
entered_words = []




db_session.global_init("db/irondle.db")


session = db_session.create_session()


random_word = session.query(Word).all()
if random_word:
    secret_word = random_word[0].iron_word
    print(secret_word)



color_map = []





@app.route('/')
def index():
    return render_template('index.html')

@app.route('/game/<int:letters>', methods=['GET', 'POST'])
def game(letters):
    if request.method == 'POST':
        word = request.form['word']
        word = word.lower()
        if len(dict_word(word).list()) == letters:
            global count_of_words_entered, attemps, secret_word, color_map
            global entered_words
            entered_words.append(dict_word(word).list())
            print(word)
            print(count_of_words_entered)
            print(entered_words)
            attemps -= 1
            count_of_words_entered += 1
            color_map.append(check_guess(word, secret_word))
            if check_guess(word, secret_word) == ['green', 'green', 'green']:
                print(color_map)
                return redirect('/viktory')
            return render_template('game.html', letters=letters, word=dict_word(word).list(),
                                   entered_words=entered_words, count_of_words_entered=count_of_words_entered,
                                   attemps=attemps, color_map=color_map)

    return render_template('game.html', letters=letters, word='='*letters, attemps=attemps, color_map=color_map, entered_words=entered_words)


def check_guess(user_word, secret_word):
    result = []

    secret_list = list(secret_word)
    user_list = list(user_word)

    secret_dict = {}
    for i, letter in enumerate(secret_list):
        if letter not in secret_dict:
            secret_dict[letter] = i

    for i in range(len(user_list)):
        letter = user_list[i]

        if letter in secret_dict:
            secret_index = secret_dict[letter]
            if i == secret_index:
                result.append('green')
            else:
                result.append('yellow')
            del secret_dict[letter]
        else:
            result.append('grey')

    return result


@app.route('/viktory')
def victory_screen():
    global color_map

    modernized_color_map = []

    for round_map in color_map:
        modernized_round = []
        for color in round_map:
            if color == 'grey':
                color = '⬛'
            elif color == 'yellow':
                color = '🟨'
            elif color == 'green':
                color = '🟩'
            modernized_round.append(color)
        modernized_color_map.append(" ".join(modernized_round))

    print("\n".join(modernized_color_map))
    modernized_color_map = "\n".join(modernized_color_map)
    return render_template('viktory.html', color_map=color_map, modernized_color_map=modernized_color_map, al='1111')



if __name__ == '__main__':
    app.run(debug=True)
