from apps import db
from flask_login import UserMixin


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    starting_capital = db.Column(db.Float, default=250000.00, nullable=False)
    oauth_github = db.Column(db.String(64), unique=True)

    def __init__(self, username, email=None, password=None, starting_capital=250000.00):
        self.username = username
        self.email = email
        self.password = password
        self.starting_capital = starting_capital


class OAuth(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    provider = db.Column(db.String(50), nullable=False)
    provider_user_id = db.Column(db.String(256), nullable=False)
    token = db.Column(db.JSON, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('Users', backref=db.backref('oauth', lazy=True))
