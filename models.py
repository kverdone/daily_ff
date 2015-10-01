from app import db

class Post(db.Model):

    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    body = db.Column(db.String)

    def __init__(self, title, body=None):
        self.title = title
        self.body = body

    def __repr__(self):
        return '<Post {}: {} --- {}>'.format(self.id, self.title, self.body)