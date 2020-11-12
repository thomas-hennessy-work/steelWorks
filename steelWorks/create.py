from application import db
from application.models import Song, Review

db.drop_all()
db.create_all()
