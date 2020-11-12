#importing the sqlalchemy object for the app
from application import db

#Creating the tables for the database
class Song(db.Model):
    song_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(127), nullable=False)
    group = db.Column(db.String(127), nullable=False)
    length = db.Column(db.Integer, nullable=False)
    yt_link = db.Column(db.String(511))
    song_review = db.relationship('Review', backref='The_review')

class Review(db.Model):
    review_id = db.Column(db.Integer, primary_key=True)
    song_id = db.Column(db.Integer, db.ForeignKey('song.song_id'), nullable=False)
    review_text = db.Column(db.String(1023), nullable=False)
    score_total = db.Column(db.Integer)
    mosh = db.Column(db.Integer)
    vocals = db.Column(db.Integer)
    riff = db.Column(db.Integer)
    bass = db.Column(db.Integer)
    beat = db.Column(db.Integer)
