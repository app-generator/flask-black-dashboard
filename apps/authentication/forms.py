from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import StringField, PasswordField, SubmitField, DecimalField
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, FloatField
from wtforms.validators import DataRequired, Email


class LoginForm(FlaskForm):
    username = StringField('Username', id='username_login',
                           validators=[DataRequired()])
    password = PasswordField('Password', id='pwd_login',
                             validators=[DataRequired()])


class CreateAccountForm(FlaskForm):
    username = StringField('Username', id='username_create',
                           validators=[DataRequired()])
    email = StringField('Email', id='email_create',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', id='pwd_create',
                             validators=[DataRequired()])
    starting_capital = FloatField(
        'Starting Capital', validators=[DataRequired()])


class CreateAccountForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[
                             DataRequired(), EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Confirm Password')
    starting_capital = DecimalField(
        'Starting Capital', default=250000.00, validators=[DataRequired()])
    submit = SubmitField('Register')
