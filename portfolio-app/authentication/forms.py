from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DecimalField
from wtforms.validators import DataRequired, Email, EqualTo


class CreateAccountForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[
                             DataRequired(), EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Confirm Password')
    starting_capital = DecimalField(
        'Starting Capital', default=250000.00, validators=[DataRequired()])
    submit = SubmitField('Register')
