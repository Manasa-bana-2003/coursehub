from flask import Flask, render_template, request, redirect, url_for, session, flash
import sys
import os
import time
import re
import psycopg2
from datetime import datetime

# Add the db module folder to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../db')))

from db import Place, User, Cart, Hotels, HotelBooking
 # Ensure these classes are correctly defined

app = Flask(__name__, static_url_path='/static')
app.secret_key = 'Manasa@2003'

# Database credentials
db_host = "localhost"
db_database = "new_db"
db_user = "manasa"
db_password = "1234"

# Constants for rate limiting
ATTEMPT_WINDOW = 300  # 5 minutes
MAX_ATTEMPTS = 5
login_attempts = {}

# Rate-limiting function
def is_rate_limited(email):
    now = time.time()
    if email not in login_attempts:
        login_attempts[email] = []
    login_attempts[email] = [timestamp for timestamp in login_attempts[email] if now - timestamp < ATTEMPT_WINDOW]
    return len(login_attempts[email]) >= MAX_ATTEMPTS

# Email validation function
def is_valid_email(email):
    regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
    return re.search(regex, email) is not None

# Routes
@app.route('/')
def home():
    user_name = session.get('user_name', None)
    place_instance = Place(db_host, db_database, db_user, db_password)
    places = place_instance.fetch_places()
    if request.method == 'POST':
        search_term = request.form.get('search')
        return redirect(url_for('search_results', search_term=search_term))
    return render_template('index.html', places=places, user_name=user_name)

@app.route('/destinations')
def destinations():
    if 'user_id' in session:
        user_name = session.get('user_name', 'Guest')
        place_instance = Place(db_host, db_database, db_user, db_password)
        places = place_instance.fetch_places()
        return render_template('destinations.html', places=places, user_name=user_name)
    else:
        flash('Please sign in first.', 'warning')
        return redirect(url_for('signin'))

@app.route('/', methods=['GET', 'POST'])
def search():
    place_instance = Place(db_host, db_database, db_user, db_password)
    places = place_instance.fetch_places()
    if request.method == 'POST':
        search_term = request.form.get('search')
        return redirect(url_for('results', search_term=search_term))
    return render_template('index.html', places=places)

@app.route('/results', methods=['GET'])
def results():
    search_term = request.args.get('search_term')
    place_instance = Place(db_host, db_database, db_user, db_password)
    places = place_instance.fetch_places(search_term)
    return render_template('search_results.html', places=places, search_term=search_term)


@app.route('/profile')
def profile():
    if 'user_id' in session:
        user_id = session['user_id']
        user_name = session.get('user_name', 'Guest')  # Retrieve user name from session

        # Fetch the user's bookings
        booking_instance = HotelBooking(db_host, db_database, db_user, db_password)
        bookings = booking_instance.get_bookings_by_user(user_id)

        # Render the profile page with user name and bookings
        return render_template('profile.html', user_name=user_name, bookings=bookings)

    else:
        flash('Please sign in first.', 'warning')
        return redirect(url_for('signin'))


@app.route('/cart')
def cart():
    if 'user_id' in session:
        cart_instance = Cart(db_host, db_database, db_user, db_password)
        cart_items = cart_instance.get_cart_items(session['user_id'])
        return render_template('cart.html', cart_items=cart_items)
    else:
        flash('Please sign in first.', 'warning')
        return redirect(url_for('signin'))

@app.route('/cart/add/<int:place_id>', methods=['POST'])
def add_to_cart(place_id):
    if 'user_id' in session:
        cart_instance = Cart(db_host, db_database, db_user, db_password)
        cart_instance.add_to_cart(session['user_id'], place_id, people=1, days=1)
        flash('Place added to cart!', 'success')
        return redirect(url_for('cart'))
    else:
        flash('Please sign in first.', 'warning')
        return redirect(url_for('signin'))

@app.route('/cart/remove/<int:place_id>', methods=['POST'])
def remove_from_cart(place_id):
    if 'user_id' in session:
        cart_instance = Cart(db_host, db_database, db_user, db_password)
        cart_instance.remove_from_cart(session['user_id'], place_id)
        flash('Place removed from cart.', 'info')
        return redirect(url_for('cart'))
    else:
        flash('Please sign in first.', 'warning')
        return redirect(url_for('signin'))

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        if not email or not is_valid_email(email):
            flash('Valid email is required.', 'danger')
            return redirect(url_for('signin'))

        if is_rate_limited(email):
            flash('Too many failed attempts. Please try again later.', 'danger')
            return redirect(url_for('signin'))

        user_instance = User(db_host, db_database, db_user, db_password)
        user_id = user_instance.authenticate(email, password)
        if user_id:
            session['user_id'] = user_id
            session['user_name'] = user_instance.get_user_name(user_id)
            return redirect(url_for('home'))
        else:
            login_attempts[email].append(time.time())
            flash('Invalid credentials. Try again.', 'danger')
            return redirect(url_for('signin'))
    return render_template('signin.html')

@app.route('/signout')
def signout():
    session.clear()
    flash('You have been signed out.', 'info')
    return redirect(url_for('signin'))

@app.route('/hotels', methods=['GET', 'POST'])
def hotels():
    hotel_instance = Hotels(db_host, db_database, db_user, db_password)
    hotels = hotel_instance.fetch_hotels()
    if request.method == 'POST':
        search_term = request.form.get('search')
        return redirect(url_for('hotel_search_results', search_term=search_term))
    return render_template('hotels/hotels.html', hotels=hotels)

@app.route('/hotel_search_results', methods=['GET'])
def hotel_search_results():
    search_term = request.args.get('search_term', '')
    hotel_instance = Hotels(db_host, db_database, db_user, db_password)
    hotels = hotel_instance.fetch_hotels(search_term)
    return render_template('hotels/hotel_search_results.html', hotels=hotels, search_term=search_term)

@app.route('/hotels/add', methods=['GET', 'POST'])
def add_hotel():
    if 'user' in session and session['role'] == 'admin':
        if request.method == 'POST':
            name = request.form['name']
            location = request.form['location']
            place = request.form['place']
            price_per_night = request.form['price_per_night']
            hotel_instance = Hotels(db_host, db_database, db_user, db_password)
            try:
                hotel_instance.add_hotel(name, location, place, price_per_night)
                flash('Hotel added successfully!', 'success')
                return redirect(url_for('hotels'))
            except Exception as e:
                flash(f'Failed to add hotel: {str(e)}', 'danger')
        return render_template('hotels/add_hotel.html')
    flash('Unauthorized access.', 'danger')
    return redirect(url_for('signin'))

@app.route('/hotels')
def hotels_redirect():
    return redirect(url_for('hotels'))


@app.route('/destinations/add', methods=['GET', 'POST'])
def add_destination():
    if 'role' in session and session['role'] == 'admin':
        if request.method == 'POST':
            name = request.form.get('name')
            location = request.form.get('location')
            description = request.form.get('description')
            cost = request.form.get('cost')
            image_url = request.form.get('image_url')

            place_instance = Place(db_host, db_database, db_user, db_password)
            place_instance.add_place(name, location, description, cost, image_url)
            flash('Place added successfully!', 'success')
            return redirect(url_for('destinations'))
        return render_template('destinations/add_destination.html')
    flash('Unauthorized access.', 'danger')
    return redirect(url_for('signin'))

from datetime import datetime

@app.route('/book_hotel', methods=['POST'])
def book_hotel():
    if 'user_id' in session:
        user_id = session['user_id']
        hotel_id = request.form.get('hotel_id')
        check_in_date = request.form.get('check_in_date')
        check_out_date = request.form.get('check_out_date')
        number_of_rooms = request.form.get('number_of_rooms')
        total_price = request.form.get('total_price')

        # Use HotelBooking instead of Hotel
        hotel_booking_instance = HotelBooking(db_host, db_database, db_user, db_password)
        hotel_booking_instance.create_booking(
            user_id=user_id,
            hotel_id=hotel_id,
            check_in_date=check_in_date,
            check_out_date=check_out_date,
            number_of_rooms=number_of_rooms,
            total_price=total_price
        )

        flash('Hotel booked successfully!', 'success')
        return redirect(url_for('profile'))
    else:
        flash('Please sign in first.', 'warning')
        return redirect(url_for('signin'))


@app.route('/search_hotels', methods=['POST'])
def search_hotels():
    check_in_date = request.form.get('check_in_date')
    check_out_date = request.form.get('check_out_date')
    number_of_rooms = int(request.form.get('number_of_rooms'))

    # Implement logic to query hotels based on availability
    # This is a placeholder for filtering logic
    available_hotels = HotelBooking.get_available_hotels(check_in_date, check_out_date, number_of_rooms)

    # Pass the available hotels to the template
    return render_template('hotels.html', hotels=available_hotels)


if __name__ == '__main__':
    app.run(debug=True)
