import unittest from flask import url_for
from flask_testing import TestCase

from app import app, db
from application.routes import index

class TestBase(TestCase):
    def create_app(self):

        app.config.update(SQLALCHEMY_DATABASE_URI=getenv('DB_URI'),
                SECRET_KEY=getenv('SECRET_KEY'),
                DEBUG=True
                )
        return app

    def setUp(self):

