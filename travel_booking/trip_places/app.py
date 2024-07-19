from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
import sys
import os

# Add the db module folder to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../db')))

from db import Places

app = Flask(__name__, static_url_path='/static')
app.secret_key = '1234'

db_host = "localhost"
db_database = "new_db"
db_user = "manasa"
db_password = "1234"

@app.route('/', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search_term = request.form.get('search_term')
        return redirect(url_for('results', search_term=search_term))
    return '''
        <form method="post" action="/">
            <input type="text" name="search_term" placeholder="Search for places">
            <input type="submit" value="Search">
        </form>
    '''

@app.route('/results', methods=['GET'])
def results():
    search_term = request.args.get('search_term')
    place_instance = Places(db_host, db_database, db_user, db_password)
    places = place_instance.fetch_places(search_term)
    return jsonify([place.__dict__ for place in places])

if __name__ == '__main__':
    app.run(debug=True, port=8080)
