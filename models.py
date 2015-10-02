from app import db

'''
class Post(db.Model):

    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    body = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

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
    posts = db.relationship('Post', backref='user')

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User {}: {} --- {}>'.format(self.id, self.username, self.email)


class Season(db.Model):

    __tablename__ = 'seasons'

    id = db.Column(db.Integer, primary_key=True)
    season_year = db.Column(db.Integer)
    weeks = db.relationship('Week', backref='season')

    def __init__(self, season_year):
        self.season_year = season_year

    def __repr__(self):
        return '<Season {}: {}>'.format(self.id, self.season_year)


class Week(db.Model):

    __tablename__ = 'weeks'

    id = db.Column(db.Integer, primary_key=True)
    week_number = db.Column(db.Integer)
    season_id = db.Column(db.Integer, db.ForeignKey('seasons.id'))

    def __init__(self, week_number):
        self.week_number = week_number

    def __repr__(self):
        return '<Week {}: {}>'.format(self.id, self.week_number)
'''

class Game(db.Model):

    __tablename__ = 'games'

    id = db.Column(db.Integer, primary_key=True)
    time_slot = db.Column(db.String)
    home_team = db.Column(db.String)
    away_team = db.Column(db.String)
    finalized = db.Column(db.Boolean)
    winner = db.Column(db.String)

    def __init__(self, time_slot, home_team, away_team, finalized=False, winner=None):
        self.time_slot = time_slot
        self.home_team = home_team
        self.away_team = away_team
        self.finalized = finalized
        self.winner = winner

    def __repr__(self):
        return '<{}> --- {} @ {}'.format(self.time_slot, self.away_team, self.home_team)
