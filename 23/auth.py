from flask import Blueprint, request, redirect, url_for, session
from models import User, db
from flask import render_template

auth_blueprint = Blueprint('auth', __name__)


@auth_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']  # Should be hashed in production
        # Check if user already exists
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            # Handle the case where the user already exists, perhaps by showing an error message
            return "User already exists", 400
        new_user = User(email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        # Redirect to the login page, or directly log the user in and redirect to the dashboard
        return redirect(url_for('auth.login'))
    # Display registration form if GET
    return render_template('register.html')


@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email, password=password).first()
        if user:
            session['user_id'] = user.id
            # Redirect to the dashboard or the desired page after successful login
            return redirect(url_for('index'))
        else:
            # Handle the case where login details are incorrect, perhaps by showing an error message
            return "Invalid credentials", 401
    # Display login form if GET
    return render_template('login.html')
