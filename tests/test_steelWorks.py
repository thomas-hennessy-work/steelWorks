import unittest 
from flask import url_for
from flask_testing import TestCase

from application import app, db
from application.routes import index
from application.models import Song

from os import getenv

class TestBase(TestCase):
    def create_app(self):

        #Used to connect to the test database rather than the live one (steelWorksTests)
        app.config.update(SQLALCHEMY_DATABASE_URI=getenv('DB_URI_TEST'),
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






class TestViews(TestBase):
    
    def test_home_get(self):
        responce = self.client.get(url_for('index'))
        self.assertEqual(responce.status_code, 200)
