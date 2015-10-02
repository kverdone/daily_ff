# Import the necessary items from flask
from flask import Flask, render_template, redirect, url_for, request, session, flash
from flask.ext.sqlalchemy import SQLAlchemy

# Create the application instance
app = Flask(__name__)

import os
app.config.from_object(os.environ['APP_SETTINGS'])
#print os.environ['APP_SETTINGS']

db = SQLAlchemy(app)

from models import *

@app.route('/')
def home():
  #posts = db.session.query(Post).all()
  games = Game.query.all()
  #return render_template('index.html', posts=posts)
  return render_template('index.html', games=games)


@app.route('/welcome')
def welcome():
  return render_template('welcome.html')

if __name__ == '__main__':
  app.run()