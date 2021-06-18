from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


@auth.route('/logout')
def logout():
    return "<h1>logout</h1>"


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        firstname = request.form.get('firstname')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(firstname) < 2:
            flash('Name Cannot be less than 2 charecters', category='error')
        elif len(email) < 4:
            flash('Email Must Be greater than 4 charecters', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match', category='error')
        elif len(password1) < 6:
            flash('Password must be atleast 6 charecters', category='error')
        else:
            # (All set) Add user to database
            flash('Successfully signed up', category='success')

    return render_template('login.html')
