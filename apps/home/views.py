# # views.py
fr# views.py
from flask import Flask, render_template, request, redirect, url_for
from yourapp import db
from yourapp.models import User
from werkzeug.security import generate_password_hash

app = Flask(__name__)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')
        starting_capital = request.form.get('starting_capital')

        hashed_password = generate_password_hash(password, method='sha256')
        new_user = User(email=email, username=username, password=hashed_password, starting_capital=starting_capital)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('authentication_blueprint.login'))

    return render_template('register.html')


 
from flask import render_template
from flask_login import login_required, current_user

@app.route('/index')
@login_required
def index():
    starting_capital = current_user.starting_capital
    return render_template('index.html', starting_capital=starting_capital)


# views.py
from flask import render_template
from flask_login import login_required, current_user

@app.route('/index')
@login_required
def index():
    starting_capital = current_user.starting_capital
    # Example portfolio data
    portfolio = [
        {"name": "Stock A", "country": "USA", "city": "New York", "value": 10000},
        {"name": "Stock B", "country": "Germany", "city": "Berlin", "value": 15000},
        {"name": "Stock C", "country": "Japan", "city": "Tokyo", "value": 20000},
    ]
    return render_template('index.html', starting_capital=starting_capital, portfolio=portfolio)