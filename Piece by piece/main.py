import random
from pprint import pprint

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

from flask import Flask, render_template, redirect, request
from data import db_session
from data.users import User
from forms.user import RegisterForm, LoginForm
from flask_login import LoginManager, login_user, login_required, logout_user

mode_value = 1  # Это значение той кнопки, которая была нажата

engine = create_engine('sqlite:///db/DataBase.db', echo=False)
Base = declarative_base()


class Animal(Base):
    __tablename__ = 'animals'
    id = Column(Integer, primary_key=True)
    mode = Column(String)
    name = Column(String)
    oset_name = Column(String)

    mode_one = relationship("ModeOne", back_populates="animal")


class ModeOne(Base):
    __tablename__ = 'mode_one'
    id = Column(Integer, primary_key=True)
    id_animal = Column(Integer, ForeignKey('animals.id'))
    tasks = Column(String)
    answers = Column(String)
    png = Column(String)

    animal = relationship("Animal", back_populates="mode_one")


Base.metadata.create_all(engine)


class ModeTwo(Base):
    __tablename__ = 'mode_two'
    id = Column(Integer, primary_key=True)
    id_animal = Column(Integer, ForeignKey('animals.id'))
    mp3 = Column(String)
    answers = Column(String)

    # animal = relationship("Animal", back_populates="mode_two")


Base.metadata.create_all(engine)


class Task:
    def __init__(self):
        self.correct_question = 0
        self.count_wrong_answer = 0
        self.lst_tasks = []
        self.lst_imgs = []

    def get_random_id(self, mode_value):
        Session = sessionmaker(bind=engine)
        session = Session()

        query = session.query(Animal.id).filter(Animal.mode == mode_value)
        self.ides = [animal[0] for animal in query.all()]

        session.close()

        return random.choice(self.ides)

    def get_tasks_by_random_id(self, random_id):
        if mode_value == 1:
            Session = sessionmaker(bind=engine)
            session = Session()

            query_tasks = session.query(ModeOne.tasks).filter(ModeOne.id_animal == random_id)
            query_answers = session.query(ModeOne.answers).filter(ModeOne.id_animal == random_id)
            query_pngs = session.query(ModeOne.png).filter(ModeOne.id_animal == random_id)

            for task, answer, png in zip(query_tasks, query_answers, query_pngs):
                lst_task = [task[0], answer[0], png[0]]
                self.lst_tasks.append(lst_task)
            session.close()

            self.texts_by_level()

            return self.lst_tasks

        elif mode_value == 2:
            Session = sessionmaker(bind=engine)
            session = Session()

            query_mp3es = session.query(ModeTwo.mp3).filter(ModeTwo.id_animal == random_id)
            query_answers = session.query(ModeTwo.answers).filter(ModeTwo.id_animal == random_id)
            for mp3, answer in zip(query_mp3es, query_answers):
                lst_task = [mp3[0], answer[0]]
                self.lst_tasks.append(lst_task)
            session.close()
            return self.lst_tasks

    def get_name_animal(self, random_id):
        Session = sessionmaker(bind=engine)
        session = Session()

        self.name_animal = session.query(Animal.oset_name).filter(Animal.id == random_id).first()
        session.close()

        return self.name_animal[0]

    def texts_by_level(self):
        if self.correct_question != len(self.lst_tasks):
            if mode_value == 1:
                list_random_wrong_words = []
                while len(list_random_wrong_words) < 3:
                    random_index = random.choice(range(len(self.lst_tasks)))
                    if random_index != self.correct_question and random_index not in list_random_wrong_words:
                        list_random_wrong_words.append(random_index)

                self.list_button_text_mode1 = [self.lst_tasks[self.correct_question][1],
                                               self.lst_tasks[list_random_wrong_words[0]][1],
                                               self.lst_tasks[list_random_wrong_words[1]][1],
                                               self.lst_tasks[list_random_wrong_words[2]][1]]
                random.shuffle(self.list_button_text_mode1)
                self.question = self.lst_tasks[task.correct_question][0]
            elif mode_value == 2:
                pass

    def restart_level(self):
        self.correct_question = 0
        self.lst_imgs.clear()


task = Task()
random_id = task.get_random_id(mode_value)
print(random_id)
task.get_tasks_by_random_id(random_id)
pprint(task.lst_tasks)

word = task.get_name_animal(random_id)

user_points_mode1 = 100

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/')
@app.route('/index')
def index():
    global user_points_mode1
    user_points_mode1 = 100  # или не тут надо

    task.restart_level()
    task.texts_by_level()  # или не тут надо, это для того чтобы когла он выходил все убиралось

    return render_template('select_level.html')


@app.route('/mode_one', methods=['GET', 'POST'])
def mode_one():
    global user_points_mode1
    if request.method == 'POST':
        selected_answer = request.form.get('btn')

        if selected_answer == task.lst_tasks[task.correct_question][1]:
            task.correct_question += 1
            task.lst_imgs.append(task.lst_tasks[task.correct_question - 1][2])
            task.count_wrong_answer = 0
            task.texts_by_level()
        else:
            task.count_wrong_answer += 1
            user_points_mode1 -= 5
            if task.count_wrong_answer == 2:
                user_points_mode1 -= 5
                task.count_wrong_answer = 0
                task.restart_level()
                task.texts_by_level()
            if user_points_mode1 < 0:
                user_points_mode1 = 0
    if request.method == 'GET':
        user_input = request.args.get('animal')

        if user_input is not None:
            if user_input == word:
                print("Уровень завершен")
            else:
                print("Неправильно!")

    return render_template('mode_one.html', question=task.question,
                           btn_texts=task.list_button_text_mode1, file_imgs=task.lst_imgs,
                           user_points=user_points_mode1, correct_question=task.correct_question,
                           len_lst_tasks=len(task.lst_tasks))


user_points_mode2 = 100


@app.route('/mode_two')
def mode_two():
    return render_template('mode_two.html', question="Послушай диктора и выбери названную им фигуру",
                           user_points=user_points_mode2)


@app.route('/about_us')
def about_us():
    return render_template('about_us.html')


@app.route('/register', methods=['GET', 'POST'])
def reqister():
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


if __name__ == '__main__':
    db_session.global_init("db/DataBase.db")
    app.run(port=8080, host='127.0.0.1')
