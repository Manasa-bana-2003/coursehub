from flask import Flask, render_template, request, redirect, url_for, session, flash
import sys
import os
import time
import re

# Add the db module folder to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../db')))

from db import Place, User  # Ensure these classes are correctly defined
# from db import Admin  # Uncomment if Admin class exists

app = Flask(__name__, static_url_path='/static')
app.secret_key = 'Manasa@2003'

db_host = "localhost"
db_database = "new_db"
db_user = "manasa"
db_password = "1234"

# Constants for rate limiting
ATTEMPT_WINDOW = 300  # 5 minutes
MAX_ATTEMPTS = 5
attempts = {}

# Rate-limiting function
def rate_limited(email):
    now = time.time()
    if email not in attempts:
        attempts[email] = []
    attempts[email] = [timestamp for timestamp in attempts[email] if now - timestamp < ATTEMPT_WINDOW]
    return len(attempts[email]) >= MAX_ATTEMPTS

# Email validation function
def valid_email(email):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
    return re.search(regex, email) is not None

# Routes
@app.route('/', methods=['GET', 'POST'])
def search():
    place_instance = Place(db_host, db_database, db_user, db_password)
    places = place_instance.fetch_places()
    if request.method == 'POST':
        search_term = request.form.get('search')
        return redirect(url_for('results', search_term=search_term))
    return render_template('index.html', places=places)

@app.route('/home')
def home():
    user_name = session.get('user_name', None)
    if user_name:
        return render_template('home.html', user_name=user_name)
    else:
        flash('You need to sign in first.')
        return redirect(url_for('signin'))

@app.route('/destinations')
def place():
    if 'user_id' in session:
        user_name = session.get('user_name', 'Guest')
        place_instance = Place(db_host, db_database, db_user, db_password)
        places = place_instance.fetch_places()
        return render_template('destinations.html', places=places, user_name=user_name)
    return redirect(url_for('signin'))

@app.route('/results', methods=['GET'])
def results():
    search_term = request.args.get('search_term')
    place_instance = Place(db_host, db_database, db_user, db_password)
    places = place_instance.fetch_places(search_term)
    return render_template('search_results.html', places=places, search_term=search_term)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        user_instance = User(db_host, db_database, db_user, db_password)
        try:
            user_instance.add_user(name, email, password)
            flash('User registered successfully')
            return redirect(url_for('signin'))
        except Exception as e:
            flash('User registration failed: ' + str(e))
            return redirect(url_for('signup'))
    return render_template('signup.html')

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user_instance = User(db_host, db_database, db_user, db_password)
        try:
            user = user_instance.verify_user(email, password)
            if user:
                session['user_id'] = email
                session['user_name'] = user['name']
                flash('User signed in successfully')
                return redirect(url_for('home'))
            else:
                flash('Invalid email or password')
        except Exception as e:
            flash('Sign-in failed: ' + str(e))
    return render_template('signin.html')

@app.route('/admin_signin', methods=['GET', 'POST'])
def admin_signin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if not valid_email(email):
            flash('Invalid email format')
            return redirect(url_for('admin_signin'))

        if rate_limited(email):
            flash('Too many login attempts. Please try again later.')
            return redirect(url_for('admin_signin'))

        # Assume Admin class exists and is correctly implemented
        # admin_instance = Admin(db_host, db_database, db_user, db_password)
        # if admin_instance.verify_user(email, password):
        #     session['user'] = email
        #     session['role'] = 'admin'
        #     return redirect(url_for('home'))
        # else:
        #     flash('Invalid email or password')
        #     return redirect(url_for('admin_signin'))
    return render_template('admin_signin.html')

@app.route('/signout')
def signout():
    session.clear()
    flash('You have been signed out.')
    return redirect(url_for('signin'))

# New routes for adding and removing places
@app.route('/destinations/add', methods=['GET', 'POST'])
def add_place():
    if 'user' in session and session['role'] == 'admin':
        if request.method == 'POST':
            name = request.form['name']
            location = request.form['location']
            description = request.form['description']

            place_instance = Place(db_host, db_database, db_user, db_password)
            try:
                place_instance.add_place(name, location, description)
                flash('Place added successfully')
                return redirect(url_for('place'))
            except Exception as e:
                flash('Failed to add place: ' + str(e))
        return render_template('add_places.html')
    flash('Unauthorized access')
    return redirect(url_for('signin'))

@app.route('/destinations/remove/<int:place_id>', methods=['POST'])
def remove_place(place_id):
    if 'user' in session and session['role'] == 'admin':
        place_instance = Place(db_host, db_database, db_user, db_password)
        try:
            place_instance.remove_place(place_id)
            flash('Place removed successfully')
        except Exception as e:
            flash('Failed to remove place: ' + str(e))
    else:
        flash('Unauthorized access')
    return redirect(url_for('place'))

if __name__ == '__main__':
    app.run(debug=True)
