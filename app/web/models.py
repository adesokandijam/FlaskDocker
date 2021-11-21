from operator import imod
from web import db

class User (db.Model):
    name = db.Column(db.String())
    id = db.Column(db.Integer, primary_key = True)