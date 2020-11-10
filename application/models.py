#importing the sqlalchemy object for the app
from application import db

#Creating the tables for the database
class Song(db.Model):
    song_id = db.Column(db.Integer, primary_key=True)
    song_title = db.Column(db.String(127), nullable=False)
    song_group = db.Column(db.String(127), nullable=False)
    song_length = db.Column(db.Integer, nullable=False)
    song_yt_link = db.Column(db.String(511))
    song_review = db.relationship('Review', backref='The_review')

class Review(db.Model):
    review_id = db.Column(db.Integer, primary_key=True)
    song_id = db.Column(db.Integer, db.ForeignKey('song.song_id'), nullable=False)
    review_text = db.Column(db.String(1023), nullable=False)
    review_score_total = db.Column(db.Integer)
    review_mosh = db.Column(db.Integer)
    review_vocals = db.Column(db.Integer)
    review_riff = db.Column(db.Integer)
    review_bass = db.Column(db.Integer)
    review_beat = db.Column(db.Integer)
