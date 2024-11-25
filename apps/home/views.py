# # views.py

# views.py# views.py
from flask import Flask, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from yourapp import db
from yourapp.models import User

@app.route('/user.html', methods=['GET', 'POST'])
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

        return redirect(url_for('user_profile'))

    return render_template('user.html')