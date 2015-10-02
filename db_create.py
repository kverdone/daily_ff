from app import db
from models import Game

db.create_all()

db.session.add(Game('Thursday', 'HOU', 'DAL', False))
db.session.add(Game('Morning', 'GB','CHI', False))
db.session.add(Game('Morning', 'OAK','SF', False))
db.session.add(Game('Afternoon', 'IND','NE', False))
db.session.add(Game('Afternoon', 'BUF','NYJ', False))
db.session.add(Game('Night', 'NYG','MIN', False))
db.session.add(Game('Night', 'ATL','SD', False))
db.session.add(Game('Monday', 'SEA','NO', False))

db.session.commit()