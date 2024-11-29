from flask_login import UserMixin
from sqlalchemy.orm import relationship
from flask_dance.consumer.storage.sqla import OAuthConsumerMixin
from apps import db, login_manager  # Import login_manager here

from apps.authentication.util import hash_pass


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    starting_capital = db.Column(db.Float, nullable=False)


class OAuth(OAuthConsumerMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    provider = db.Column(db.String(50), nullable=False)
    provider_user_id = db.Column(db.String(256), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(Users.id), nullable=False)
    user = db.relationship(Users)


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))
