from app import db

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Post(db.Model):

    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    body = db.Column(db.String)
    user_id = db.Column(db.Integer, ForeignKey('users.id'))

    def __init__(self, title, body=None):
        self.title = title
        self.body = body

    def __repr__(self):
        return '<Post {}: {} --- {}>'.format(self.id, self.title, self.body)

class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    posts = relationship('Post', backref='user')

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User {}: {} --- {}>'.format(self.id, self.username, self.email)