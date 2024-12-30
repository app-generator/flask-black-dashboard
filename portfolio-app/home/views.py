
from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from apps import db
from apps.authentication.models import Users

home = Blueprint('home', __name__)


@home.route('/')
def index():
    return render_template('index.html')


@home.route('/user.html', methods=['GET', 'POST'])
@login_required
def user_profile():
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        starting_capital = request.form.get('starting_capital')

        current_user.email = email
        current_user.username = username
        current_user.starting_capital = starting_capital
        db.session.commit()

        return redirect(url_for('home.user_profile'))

    return render_template('user.html')
