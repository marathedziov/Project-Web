import sqlalchemy
from sqlalchemy import orm





from .db_session import SqlAlchemyBase

class Categori(SqlAlchemyBase):
    __tablename__ = 'category'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    iron_name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    russian_name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
