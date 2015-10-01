from app import db
from models import Post

db.create_all()

db.session.add(Post('Good', 'This is good.'))
db.session.add(Post('App', 'Making an app!'))


db.session.commit()