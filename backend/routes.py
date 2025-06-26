from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import db, User

main = Blueprint('main', __name__)

@main.route('/')
def home():
    users = User.query.all()
    return render_template('home.html', users=users)

@main.route('/add_user', methods=['POST'])
def add_user():
    username = request.form.get('username')
    email = request.form.get('email')
    if username and email:
        user = User(username=username, email=email)
        db.session.add(user)
        db.session.commit()
        flash('User added successfully!', 'success')
    else:
        flash('Please provide both username and email.', 'danger')
    return redirect(url_for('main.home'))