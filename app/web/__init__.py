from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://dijam:dijam@postgre:5432/dijam'
app.config['SECRET_KEY'] = 'HARD TO GUESS THE STRING'
db =SQLAlchemy(app)

from web import routes