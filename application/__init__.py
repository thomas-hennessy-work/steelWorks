from flask import Flask
#Used to to link the database layer to the application
from flask_sqlalchemy import SQLAlchemy

#Used for environment variables (so that Ben wont hack the server)
from os import getenv

app = Flask(__name__)
app.config['SECRET_KEY'] = getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"

db = SQLAlchemy(app)

from application import routes
