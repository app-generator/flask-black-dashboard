from flask import redirect, url_for, flash
from flask_dance.consumer import oauth_authorized, oauth_error
from flask_dance.contrib.github import make_github_blueprint, github
from flask_login import current_user, login_user, logout_user
from sqlalchemy.orm.exc import NoResultFound
from apps.config import Config
from apps import db  # Import only db here
from .models import Users, OAuth  # Import models here

github_blueprint = make_github_blueprint(
    client_id=Config.GITHUB_ID,
    client_secret=Config.GITHUB_SECRET,
)


@oauth_authorized.connect_via(github_blueprint)
def github_logged_in(blueprint, token):
    info = github.get("/user")

    if info.ok:
        account_info = info.json()
        username = account_info["login"]

        query = Users.query.filter_by(oauth_github=username)
        try:
            user = query.one()
            login_user(user)
        except NoResultFound:
            # Save to db
            user = Users(username='(gh)' + username, oauth_github=username)
            db.session.add(user)
            db.session.commit()
            login_user(user)

# Error handling for OAuth


@oauth_error.connect_via(github_blueprint)
def github_error(blueprint, message, response):
    flash(f"OAuth error from {blueprint.name}! message={
          message} response={response}", category="error")
