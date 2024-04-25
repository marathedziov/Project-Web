from flask import Flask, render_template, redirect, request, session
from data import db_session
from data.categories import Category
from data.crosswords import Crosswords
from data.users import User
from data.words import Words
from forms.user import RegisterForm, LoginForm
from flask_login import LoginManager, login_user, logout_user, login_required, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route("/")
def index():
    session["cur_cross"] = 1
    session["guessed"] = list()
    db_sess = db_session.create_session()
    cats = db_sess.query(Category)
    return render_template("index.html", cats=cats, current_user=current_user)


@app.route("/crosswords", methods=['POST', 'GET'])
def chose_cross():
    session['guessed'] = []
    cat_id = request.form.get('cat')
    db_sess = db_session.create_session()
    crossds = db_sess.query(Crosswords).filter(Crosswords.id_category == cat_id)
    return render_template("chose_cross.html", crossds=crossds)


@app.route("/crosswords/<int:id>")
def crossword(id):
    session["cur_cross"] = id
    matrix = [[''] * 10 for i in range(10)]
    db_sess = db_session.create_session()
    words = db_sess.query(Words).filter(Words.id_cross == id)
    descr = list(map(lambda x: x.description, words))
    ans = db_sess.query(Crosswords).filter(Crosswords.id == id).first()

    for ind, cross in enumerate(words):
        word = cross.word_iron.split()
        x, y = map(int, cross.coords.split())
        place = int(cross.place)
        f = False
        guessed = session.get('guessed')
        if word in guessed:
            f = True
        for i in range(len(word)):
            cell = word[i]
            if f:
                cell = cell.lower()
            if i == 0:
                matrix[y][x - 1] = (str(ind + 1), cross.id, 'num')
            if i == place:
                matrix[y][x + i] = (cell, 'bold_td')
            else:
                matrix[y][x + i] = (cell, 'td')

    return render_template("crossword.html", cross=matrix, descr=descr, ans=ans.word_ans_rus)


@app.route('/add_word<int:id>')
def ans(id):
    db_sess = db_session.create_session()
    print(session.get('cur_cross'))
    ans = db_sess.query(Words).filter(Words.id_cross == int(session.get('cur_cross')),
                                      Words.id == id).first()
    return render_template('check.html', ans=ans)


@app.route(f'/check/<int:id>', methods=['POST', 'GET'])
def check(id):
    cur_cross = session.get("cur_cross")
    res = request.form.get(str(id)).upper().replace('АЕ', 'Æ')
    word = request.form.get('word').split()
    if res == ''.join(word):
        guessed = session.get('guessed')
        guessed.append(word)
        session["guessed"] = guessed
    return redirect(f'/crosswords/{cur_cross}')


@app.route(f'/final_check', methods=['POST'])
def final_check():
    cur_cross = session.get("cur_cross")
    quest = request.form.get('quest').upper()
    ans = request.form.get('ans')
    if quest == ans:
        return redirect('/victory')
    return redirect(f'/crosswords/{cur_cross}')


@app.route("/victory")
def victory():
    return render_template("victory.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            email=form.email.data,
            about=form.about.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/')
    return render_template('register.html', title='Регистрация', form=form)


def main():
    db_session.global_init("db/crosswords.db")


if __name__ == '__main__':
    main()
    app.run(host='0.0.0.0', port=8003)
