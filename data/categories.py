import sqlalchemy

from .db_session import SqlAlchemyBase


class Category(SqlAlchemyBase):
    __tablename__ = 'categories'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    category_iron = sqlalchemy.Column(sqlalchemy.String)
    category_rus = sqlalchemy.Column(sqlalchemy.String)
