import sqlalchemy

from .db_session import SqlAlchemyBase


class Words(SqlAlchemyBase):
    __tablename__ = 'words'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    word_iron = sqlalchemy.Column(sqlalchemy.String)
    description = sqlalchemy.Column(sqlalchemy.String)
    word_rus = sqlalchemy.Column(sqlalchemy.String)
    place = sqlalchemy.Column(sqlalchemy.Integer)
    coords = sqlalchemy.Column(sqlalchemy.String)
    id_cross = sqlalchemy.Column(sqlalchemy.Integer,
                                 sqlalchemy.ForeignKey("crosswords.id"))
