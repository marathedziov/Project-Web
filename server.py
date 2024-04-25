from flask import Flask, render_template, request, redirect, session
from lib_iron.class_sort_iron import dict_word
from data import db_session
from data.word import Word
import time

# time.sleep(5)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'






def create_cookies():
    session["attempts"] = 7
    session["secret_word"] = ""
    session["entered_words"] = []
    session["color_map"] = []
    session["the_guessed_words"] = []
    session["letters"] = 3
    session["count_of_games"] = 0




def guess_word(letters):
    db_session.global_init("db/irondle.db")

    session_db_ = db_session.create_session()

    all_words = session_db_.query(Word).all()
    for i in all_words:
        if len(dict_word(i.iron_word).list()) == letters:
            print(i.iron_word)
            secret_word = i.iron_word
            the_guessed_words = session.get("the_guessed_words")
            if secret_word not in the_guessed_words:
                session["secret_word"] = secret_word
                print(secret_word)





@app.route('/')
def index():
    create_cookies()

    return render_template('index.html')


@app.route('/game/<int:letters>', methods=['GET', 'POST'])
def game(letters):
    guess_word(letters)

    count_of_games = int(session.get("count_of_games")) + 1
    session["count_of_games"] = count_of_games

    if request.method == 'POST':
        word = request.form['word']
        word = word.lower()
        if len(dict_word(word).list()) == letters:
            attempts = int(session.get("attempts"))
            attempts -= 1
            print(attempts)

            session["attempts"] = attempts
            if attempts > 0:

                entered_words = session.get("entered_words")
                entered_words.append(dict_word(word).list())
                session["entered_words"] = entered_words

                print(word)





                secret_word = session.get('secret_word')
                color_map = session.get('color_map')

                color_map.append(check_guess(word, secret_word))

                session["color_map"] = color_map



                if check_guess(word, secret_word) == ['green'] * letters:
                    print(color_map)
                    time.sleep(2)
                    return redirect('/viktory')

                attempts = int(session.get("attempts"))

                return render_template('game.html', letters=letters, word=dict_word(word).list(),
                                       entered_words=entered_words,
                                       attemps=attempts, color_map=color_map)
            else:
                time.sleep(2)
                return render_template('lose.html')
    entered_words = session.get("entered_words")
    color_map = session.get("color_map")

    return render_template('game.html', letters=letters, word='='*letters, attemps=int(session.get("attempts")), color_map=color_map, entered_words=entered_words)


def check_guess(user_word, secret_word):
    result = []

    secret_list = dict_word(secret_word).list()
    user_list = dict_word(user_word).list()
    print(secret_list, "||", user_list)

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

    color_map = session.get("color_map")

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
    letters = session.get("letters")

    return render_template('viktory.html', color_map=color_map, modernized_color_map=modernized_color_map, letters=letters, al='1111')



if __name__ == '__main__':
    app.run()
