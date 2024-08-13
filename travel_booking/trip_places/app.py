from flask import Flask, render_template, request, redirect, url_for, session, flash
import sys
import os

# Add the db module folder to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../db')))

from db import Places, users1

app = Flask(__name__, static_url_path='/static')
app.secret_key = 'Manasa@2003'

db_host = "localhost"
db_database = "new_db"
db_user = "manasa"
db_password = "1234"

@app.route('/', methods=['GET', 'POST'])
def search():
    place_instance = Places(db_host, db_database, db_user, db_password)
    places = place_instance.fetch_places()

    if request.method == 'POST':
        search_term = request.form.get('search')
        return redirect(url_for('results', search_term=search_term))
    return render_template('index.html', places=places)

@app.route('/home')
def home():
    if 'user_id' in session:
        user_name = session['user_name']
        role = session.get('role', 'User')  # Default role if not set
        return render_template('index.html', user_name=user_name, role=role)
    return redirect(url_for('signin'))

@app.route('/destinations')
def place():
    if 'user_id' in session:
        user_name = session['user_name']
        place_instance = Places(db_host, db_database, db_user, db_password)
        places = place_instance.fetch_places()
        return render_template('destinations.html', places=places, user_name=user_name)
    return redirect(url_for('signin'))

@app.route('/results', methods=['GET'])
def results():
    search_term = request.args.get('search_term')
    place_instance = Places(db_host, db_database, db_user, db_password)
    places = place_instance.fetch_places(search_term)
    return render_template('search_results.html', places=places, search_term=search_term)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        user_instance = users1(db_host, db_database, db_user, db_password)
        try:
            print("Adding user: ", name, email)
            user_instance.add_user(name, email, password)
            flash('User registered successfully')
            print("User registered successfully")
            return redirect(url_for('signin'))
        except Exception as e:
            print("Error: ", str(e))
            flash('User registration failed: ' + str(e))
            return redirect(url_for('signup'))
    return render_template('signup.html')

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user_instance = users1(db_host, db_database, db_user, db_password)
        try:
            print("Signing in user: ", email)
            user = user_instance.authenticate_user(email, password)
            if user:
                # Using session for user authentication
                session['user_id'] = user['id']
                session['user_name'] = user['name']
                flash('User signed in successfully')
                print("User signed in successfully")
                return redirect(url_for('home'))  # Redirect to home after signin
            else:
                flash('Invalid email or password')
                print("Invalid email or password")
                return redirect(url_for('signin'))
        except Exception as e:
            print("Error: ", str(e))
            flash('Sign-in failed: ' + str(e))
            return redirect(url_for('signin'))
    return render_template('signin.html')

@app.route('/signout')
def signout():
    session.clear()  # Clear the session to log out the user
    flash('You have been signed out.')
    return redirect(url_for('signin'))

if __name__ == '__main__':
    app.run(debug=True)
