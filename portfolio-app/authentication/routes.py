from flask import render_template, redirect, request, url_for, Blueprint
from flask_login import current_user, login_user, logout_user
from apps import db, login_manager
from apps.authentication import blueprint
from apps.authentication.forms import LoginForm, CreateAccountForm
from apps.authentication.models import Users
from apps.authentication.util import verify_pass

# Define the home blueprint
home = Blueprint('home', __name__)


@home.route('/')
def index():
    return render_template('index.html')


@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm(request.form)
    if 'login' in request.form:
        username = request.form['username']
        password = request.form['password']
        user = Users.query.filter_by(username=username).first()
        if user and verify_pass(password, user.password):
            login_user(user)
            return redirect(url_for('home.index'))
        return render_template('accounts/login.html', msg='Wrong user or password', form=login_form)
    if not current_user.is_authenticated:
        return render_template('accounts/login.html', form=login_form)
    return redirect(url_for('home.index'))


@blueprint.route('/register', methods=['GET', 'POST'])
def register():
    create_account_form = CreateAccountForm(request.form)
    if 'register' in request.form:
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        starting_capital = request.form.get('starting_capital', 250000.00)
        user = Users.query.filter_by(username=username).first()
        if user:
            return render_template('accounts/register.html', msg='Username already registered', success=False, form=create_account_form)
        user = Users.query.filter_by(email=email).first()
        if user:
            return render_template('accounts/register.html', msg='Email already registered', success=False, form=create_account_form)
        user = Users(username=username, email=email,
                     password=password, starting_capital=starting_capital)
        db.session.add(user)
        db.session.commit()
        logout_user()
        return render_template('accounts/register.html', msg='Account created successfully.', success=True, form=create_account_form)
    return render_template('accounts/register.html', form=create_account_form)


@blueprint.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('authentication_blueprint.login'))

# Error handlers


@login_manager.unauthorized_handler
def unauthorized_handler():
    return render_template('home/page-403.html'), 403


@blueprint.errorhandler(403)
def access_forbidden(error):
    return render_template('home/page-403.html'), 403


@blueprint.errorhandler(404)
def not_found_error(error):
    return render_template('home/page-404.html'), 404


@blueprint.errorhandler(500)
def internal_error(error):
    return render_template('home/page-500.html'), 500
