import sqlalchemy

from .db_session import SqlAlchemyBase


class Crosswords(SqlAlchemyBase):
    __tablename__ = 'crosswords'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    word_ans_iron = sqlalchemy.Column(sqlalchemy.String)
    word_ans_rus = sqlalchemy.Column(sqlalchemy.String)
    id_category = sqlalchemy.Column(sqlalchemy.Integer,
                                    sqlalchemy.ForeignKey("categories.id"))
