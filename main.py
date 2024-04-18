import pprint

from flask import Flask, render_template, redirect, request, abort
from data import db_session
from data.crosswords import Crosswords
from data.users import User
from data.news import News
from data.words import Words
from forms.news import NewsForm
from forms.user import RegisterForm, LoginForm
from flask_login import LoginManager, login_user, logout_user, login_required, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)

guessed = []


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


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


@app.route("/")
def index():
    return render_template("start.html", current_user=current_user)


@app.route("/crossword1")
def crossword():
    matrix = [[''] * 9 for i in range(9)]
    db_sess = db_session.create_session()
    crossds = db_sess.query(Words).filter(Words.id_cross == 1)
    descr = list(map(lambda x: x.description, crossds))

    for ind, cross in enumerate(crossds):
        global guessed
        word = cross.word_iron.split()
        # guessed.append(word)
        x, y = map(int, cross.coords.split())
        place = int(cross.place)
        f = False
        if word in guessed:
            f = True
        for i in range(len(word)):
            cell = word[i]
            if f:
                cell = cell.lower()
            if i == 0:
                matrix[y][x - 1] = (str(ind + 1), 'num')
            if i == place:
                matrix[y][x + i] = (cell, 'bold_td')

            else:
                matrix[y][x + i] = (cell, 'td')

    pprint.pprint(matrix)
    return render_template("index.html", cross=matrix, descr=descr)


@app.route('/check', methods=['GET', 'POST'])
def check():
    if request.method == 'POST':
        res = request.form['ans']
        return render_template("index.html", res=res)
    return redirect('/crossword1')


@app.route('/add_word/<int:id>', methods=['GET', 'POST'])
def check_ans(id):
    db_sess = db_session.create_session()
    ans = db_sess.query(Words).filter(Words.id_cross == 1,
                                      Words.id == id).first()
    return render_template('check.html', ans=ans)


@app.route('/news', methods=['GET', 'POST'])
@login_required
def add_news():
    form = NewsForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        news = News()
        news.title = form.title.data
        news.content = form.content.data
        news.is_private = form.is_private.data
        current_user.news.append(news)
        db_sess.merge(current_user)
        db_sess.commit()
        return redirect('/')
    return render_template('news.html', title='Добавление новости',
                           form=form)


@app.route('/news/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_news(id):
    form = NewsForm()
    if request.method == "GET":
        db_sess = db_session.create_session()
        news = db_sess.query(News).filter(News.id == id,
                                          News.user == current_user
                                          ).first()
        if news:
            form.title.data = news.title
            form.content.data = news.content
            form.is_private.data = news.is_private
        else:
            abort(404)
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        news = db_sess.query(News).filter(News.id == id,
                                          News.user == current_user
                                          ).first()
        if news:
            news.title = form.title.data
            news.content = form.content.data
            news.is_private = form.is_private.data
            db_sess.commit()
            return redirect('/')
        else:
            abort(404)
    return render_template('news.html',
                           title='Редактирование новости',
                           form=form
                           )


@app.route('/news_delete/<int:id>', methods=['GET', 'POST'])
@login_required
def news_delete(id):
    db_sess = db_session.create_session()
    news = db_sess.query(News).filter(News.id == id,
                                      News.user == current_user
                                      ).first()
    if news:
        db_sess.delete(news)
        db_sess.commit()
    else:
        abort(404)
    return redirect('/')


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
    app.run()


if __name__ == '__main__':
    main()
