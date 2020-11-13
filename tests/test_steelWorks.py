import unittest 
from flask import url_for
from flask_testing import TestCase

from application import app, db
from application.routes import index
from application.models import Song, Review

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

        sampleReview = Review(song_id=1,
                review_text="Good song, I liked it",
                score_total=9,
                mosh=7,
                vocals=8,
                riff=6,
                bass=8,
                beat=10)
        
        db.session.add(sampleSong)
        db.session.add(sampleReview)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()






class TestViews(TestBase):
    
    def test_index_get(self):
        responce = self.client.get(url_for('index'))
        self.assertEqual(responce.status_code, 200)

    def test_addSong_get(self):
        responce = self.client.get(url_for('addSong'))
        self.assertEqual(responce.status_code, 200)

    def test_addSong_post(self):
        responce = self.client.post(url_for('addSong'))
        self.assertEqual(responce.status_code, 200)

    def test_addReview_get(self):
        responce = self.client.get(url_for('addReview', songID=1))
        self.assertEqual(responce.status_code, 200)

    def test_addReview_get(self):
        responce = self.client.get(url_for('addReview', songID=1))
        self.assertEqual(responce.status_code, 200)

    def test_addReview_post(self):
        responce = self.client.post(url_for('addReview', songID=1))
        self.assertEqual(responce.status_code, 200)

    def test_viewSong_get(self):
        responce = self.client.get(url_for('viewSong', songID=1))
        self.assertEqual(responce.status_code, 200)

    def test_editSong_get(self):
        responce = self.client.get(url_for('editSong', songID=1))
        self.assertEqual(responce.status_code, 200)

    def test_editSong_post(self):
        responce = self.client.post(url_for('editSong', songID=1))
        self.assertEqual(responce.status_code, 200)

    def test_deleteSong_get(self):
        responce = self.client.get(url_for('deleteSong', songID=1))
        self.assertEqual(responce.status_code, 302)

    def test_deleteReview_get(self):
        responce = self.client.get(url_for('deleteReview', reviewID=1))
        self.assertEqual(responce.status_code, 302)





class TestSongCRUD(TestBase):

    def test_add_song(self):
        responce = self.client.post(url_for('addSong'),
                data = dict(title="Redfog",
                            group="Orbit culture",
                            length=358,
                            youTube="https://www.youtube.com/embed/la21crvpjpk")
                )
        #Needs a bytes type object, hence the b
        self.assertIn(b"Redfog",responce.data)
        self.assertIn(b"Orbit culture",responce.data)
        self.assertIn(b"358",responce.data)
        self.assertIn(b"https://www.youtube.com/embed/la21crvpjpk",responce.data)

    def test_update_song(self):
        songID=1
        responce = self.client.post(url_for('editSong', songID=songID),
                data = dict(title="Retrospection",
                            group="Jinjer",
                            length=294,
                            youTube="https://www.youtube.com/embed/Wh2yOebcENM")
                )
        self.assertIn(b"Retrospection",responce.data)
        self.assertIn(b"Jinjer",responce.data)
        self.assertIn(b"294",responce.data)
        self.assertIn(b"https://www.youtube.com/embed/Wh2yOebcENM",responce.data)
