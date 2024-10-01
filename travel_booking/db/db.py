import psycopg2
from psycopg2 import sql
from werkzeug.security import generate_password_hash, check_password_hash
import logging

# Set up logging for debugging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Class to handle database connections
class DatabaseConnection:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = None

    def __enter__(self):
        self.connection = psycopg2.connect(
            host=self.host,
            database=self.database,
            user=self.user,
            password=self.password
        )
        return self.connection

    def __exit__(self, exc_type, exc_value, traceback):
        if self.connection:
            self.connection.close()
        if exc_type is not None:
            logger.error("Exception occurred: %s", exc_value)
        print("Database connection closed.")

# Class to manage places in the database
class Place:
    def __init__(self, host, database, user, password):
        self.db_params = (host, database, user, password)

    def fetch_places(self, search_term=None):
        with DatabaseConnection(*self.db_params) as conn:
            cursor = conn.cursor()
            query = "SELECT * FROM place"
            if search_term:
                query += " WHERE name ILIKE %s OR location ILIKE %s"
                cursor.execute(query, (f'%{search_term}%', f'%{search_term}%'))
            else:
                cursor.execute(query)
            places_data = cursor.fetchall()
            cursor.close()
        places = [PlaceDetails(*place_data) for place_data in places_data]
        return places

    def get_place_by_id(self, place_id):
        with DatabaseConnection(*self.db_params) as conn:
            cursor = conn.cursor()
            query = "SELECT * FROM place WHERE place_id = %s"
            cursor.execute(query, (place_id,))
            place_data = cursor.fetchone()
            cursor.close()
        if place_data:
            return PlaceDetails(*place_data)
        return None

    def add_place(self, name, location, description, cost):
        with DatabaseConnection(*self.db_params) as conn:
            cursor = conn.cursor()
            query = """
                INSERT INTO place (name, location, description, cost)
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(query, (name, location, description, cost))
            conn.commit()
            cursor.close()

    def remove_place(self, place_id):
        with DatabaseConnection(*self.db_params) as conn:
            cursor = conn.cursor()
            query = "DELETE FROM place WHERE place_id = %s"
            cursor.execute(query, (place_id,))
            conn.commit()
            cursor.close()

# Class to hold place details
class PlaceDetails:
    def __init__(self, place_id, name, location, description, cost, history=None):
        self.id = place_id
        self.name = name
        self.location = location
        self.description = description
        self.cost = cost
        self.history = history or ""

    def __str__(self):
        return (f"place_id: {self.id}, Name: {self.name}, Description: {self.description[:60]}..., "
                f"Location: {self.location}, Cost: {self.cost}")

# Class to manage user operations in the database
class User:
    def __init__(self, host, database, user, password):
        self.db_params = (host, database, user, password)

    def add_user(self, name, email, password):
        with DatabaseConnection(*self.db_params) as conn:
            cursor = conn.cursor()
            hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
            query = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
            try:
                cursor.execute(query, (name, email, hashed_password))
                conn.commit()
            except Exception as e:
                conn.rollback()
                logger.error("Error adding user: %s", str(e))
                raise e
            finally:
                cursor.close()

    def verify_user(self, email, password):
        with DatabaseConnection(*self.db_params) as conn:
            cursor = conn.cursor()
            query = "SELECT password FROM users WHERE email = %s"
            cursor.execute(query, (email,))
            result = cursor.fetchone()
            cursor.close()
        if result and check_password_hash(result[0], password):
            return True
        return False

    def get_user(self, email):
        with DatabaseConnection(*self.db_params) as conn:
            cursor = conn.cursor()
            query = "SELECT name, email FROM users WHERE email = %s"
            cursor.execute(query, (email,))
            result = cursor.fetchone()
            cursor.close()
        if result:
            return {"name": result[0], "email": result[1]}
        return None

    def update_user(self, current_email, name, email, password):
        with DatabaseConnection(*self.db_params) as conn:
            cursor = conn.cursor()
            hashed_password = generate_password_hash(password) if password else None
            query = "UPDATE users SET name = %s, email = %s"
            params = [name, email]
            if hashed_password:
                query += ", password = %s"
                params.append(hashed_password)
            query += " WHERE email = %s"
            params.append(current_email)
            try:
                cursor.execute(query, tuple(params))
                conn.commit()
            except Exception as e:
                conn.rollback()
                logger.error("Error updating user: %s", str(e))
                raise e
            finally:
                cursor.close()

# Class to manage cart operations in the database
class Cart:
    def __init__(self, host, database, user, password):
        self.db_params = (host, database, user, password)

    def add_to_cart(self, user_id, place_id, people, days):
        with DatabaseConnection(*self.db_params) as conn:
            cursor = conn.cursor()
            query = """
                INSERT INTO cart (user_id, place_id, people, days)
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(query, (user_id, place_id, people, days))
            conn.commit()
            cursor.close()

    def remove_from_cart(self, user_id, place_id):
        with DatabaseConnection(*self.db_params) as conn:
            cursor = conn.cursor()
            query = "DELETE FROM cart WHERE user_id = %s AND place_id = %s"
            cursor.execute(query, (user_id, place_id))
            conn.commit()
            cursor.close()

    def get_cart_items(self, user_id):
        with DatabaseConnection(*self.db_params) as conn:
            cursor = conn.cursor()
            query = """
                SELECT p.name, p.description, p.location, c.people, c.days
                FROM cart c
                JOIN place p ON c.place_id = p.place_id
                WHERE c.user_id = %s
            """
            cursor.execute(query, (user_id,))
            cart_items = cursor.fetchall()
            cursor.close()
        return cart_items
