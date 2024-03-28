import sqlalchemy
from sqlalchemy.orm import sessionmaker

from data import db_session
from data.word import Word



db_session.global_init("db/irondle.db")


session = db_session.create_session()


first_word = session.query(Word).all()
if first_word:
    print(first_word[0].iron_word)

