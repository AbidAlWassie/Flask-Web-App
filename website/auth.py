from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect Password! try again.', category='error')
        else:
            flash('Email does not exist!', category='error')

    return render_template('login.html')


@auth.route('/logout')
def logout():
    return "<h1>logout</h1>"


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        full_name = request.form.get('full_name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()

        if user:
            flash('Email already exist!', category='error')
        elif len(full_name) < 2:
            flash('Name Cannot be less than 2 charecters', category='error')
        elif len(email) < 4:
            flash('Email Must Be greater than 4 charecters', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match', category='error')
        elif len(password1) < 6:
            flash('Password must be atleast 6 charecters', category='error')
        else:
            new_user = User(email=email, full_name=full_name, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Successfully signed up', category='success')
            return redirect(url_for('views.home'))

    return render_template('login.html')
