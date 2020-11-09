from flas import Flask
#Used to to link the database layer to the application
from flask_sqlalchemy import SQLAlchemy

#Used for environment variables (so that Ben wont hack the server)
from os import getenv

app = Flask(__name__)
app.config['SECRET_KEY'] = getenv('SECRET_KEY')

db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DB_URI')
from application import routes
