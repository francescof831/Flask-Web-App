from email.policy import default
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

#since one user can have many notes, Note has a foreign key to reference its user
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) #user must be lowercase because you are referencing table


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note') #this line is so you can get all of a user's notes - "Note" has to be capital since you are referencing name of the class
