import unittest from flask import url_for
from flask_testing import TestCase

from app import app, db
from application.routes import index
from application.models import Song

class TestBase(TestCase):
    def create_app(self):

        app.config.update(SQLALCHEMY_DATABASE_URI=getenv('DB_URI'),
                SECRET_KEY=getenv('SECRET_KEY'),
                DEBUG=True
                )
        return app

    #Used before every test to set up a test song
    def setUp(self):
        db.create_all()

        sampleSong = Song(title="Pisces", 
                group="Jinjer",
                length=305,
                yt_link="https://www.youtube.com/embed/SQNtGoM3FVU")

        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
