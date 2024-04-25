import json

from flask import Flask, request, redirect, session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

@app.route('/')
def index():
    session["current_question"] = [1, 2, 3]
    current_question = session.get("current_question", [])
    print(current_question)



    return "asdgasdgsdfgssdfg"


if __name__ == '__main__':
    app.run()