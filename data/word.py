import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase

class Word(SqlAlchemyBase):
    __tablename__ = 'word'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    iron_word = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    russian_word = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    category_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("categori.id"))
    category_ = orm.relationship('Categori')