from app import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)


class Users(db.Model):
    __tablename__ = 'users'

    user_name = db.Column(db.String(), primary_key=True)
    group_name = db.Column(db.String())

    def __init__(self, user_name, group_name):
        self.user_name = user_name
        self.group_name = group_name
