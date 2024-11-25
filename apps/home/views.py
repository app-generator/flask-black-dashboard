# # views.py

# views.py
from flask import Flask, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from yourapp import db
from yourapp.models import User

@app.route('/update_user', methods=['POST'])
@login_required
def update_user():
    email = request.form.get('email')
    username = request.form.get('username')
    starting_capital = request.form.get('starting_capital')

    current_user.email = email
    current_user.username = username
    current_user.starting_capital = starting_capital
    db.session.commit()

    return redirect(url_for('user_profile'))

@app.route('/user.html')
@login_required
def user_profile():
    return render_template('user.html')
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