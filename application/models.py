#importing the sqlalchemy object for the app
from application import db

class Song(db.Model):
    song_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(127), nullable=False)
    group = db.Column(db.String(127), nullable=False)
    length = db.Column(db.Integer, nullable=False)
    yt_link = db.Column(db.String(511))

class Review(db.Model):
    review_id = db.Column(db.Integer, primary_key=True)
    review_text = db.Column(db.String(1023), nullable=False)
    score_total = db.Column(db.integer)
    mosh = db.Column(db.integer)
    vocals = db.Column(db.integer)
    riff = db.Column(db.integer)
    bass = db.Column(db.integer)
    beat = db.Column(db.integer)
