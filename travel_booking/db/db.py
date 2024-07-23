import psycopg2
from psycopg2 import sql
from werkzeug.security import generate_password_hash, check_password_hash
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

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

class PlaceDetails:
    def __init__(self, place_id, name,location,description):
        self.id = place_id
        self.name = name
        self.location = location
        self.description = description


    def __str__(self):
        return (f"place_id: {self.id}, Name: {self.name}, Description: {self.desc[:60]}..., "
                f"Location: {self.location}")


class Places:
    def __init__(self, host, database, user, password):
        self.db_params = (host, database, user, password)

    def fetch_places(self, search_term=None):
        with DatabaseConnection(*self.db_params) as conn:
            cursor = conn.cursor()
            query = "SELECT * FROM place"
            if search_term:
                query += " WHERE name ILIKE %s"
                cursor.execute(query, (f'{search_term}%',))  # Modified line to search for places starting with the search term
            else:
                cursor.execute(query)
            places_data =  cursor.fetchall()
            cursor.close()
        places = [PlaceDetails(*place_data) for place_data in places_data]
        return places

    def add_place(self,name,location,description):
        with DatabaseConnection(*self.db_params) as conn:
            cursor = conn.cursor()
            query = """
                INSERT INTO place (name,location,description)
                VALUES (%s, %s, %s)
            """
            cursor.execute(query, (name,location, description))
            conn.commit()
            cursor.close()

    def remove_place(self, course_id):
        with DatabaseConnection(*self.db_params) as conn:
            cursor = conn.cursor()
            query = "DELETE FROM place WHERE id = %s"
            cursor.execute(query, (course_id,))
            conn.commit()
            cursor.close()


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

    def add_course_to_profile(self, user_email, course_id):
        with DatabaseConnection(*self.db_params) as conn:
            cursor = conn.cursor()
            query = "INSERT INTO user_courses (user_email, course_id) VALUES (%s, %s)"
            try:
                cursor.execute(query, (user_email, course_id))
                conn.commit()
            except Exception as e:
                conn.rollback()
                logger.error("Error adding course to profile: %s", str(e))
                raise e
            finally:
                cursor.close()

    def get_user_courses(self, user_email):
        with DatabaseConnection(*self.db_params) as conn:
            cursor = conn.cursor()
            query = """
                   SELECT courses.id, courses.name, courses.description
                   FROM courses
                   JOIN user_courses ON courses.id = user_courses.course_id
                   WHERE user_courses.user_email = %s
               """
            cursor.execute(query, (user_email,))
            result = cursor.fetchall()
            cursor.close()
        return result


class Admin:
    def __init__(self, host, database, user, password):
        self.db_params = (host, database, user, password)

    def add_user(self, name, email, password):
        with DatabaseConnection(*self.db_params) as conn:
            cursor = conn.cursor()
            hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
            query = "INSERT INTO admin (name, email, password) VALUES (%s, %s, %s)"
            try:
                cursor.execute(query, (name, email, hashed_password))
                conn.commit()
            except Exception as e:
                conn.rollback()
                logger.error("Error adding admin: %s", str(e))
                raise e
            finally:
                cursor.close()

    def verify_user(self, email, password):
        with DatabaseConnection(*self.db_params) as conn:
            cursor = conn.cursor()
            query = "SELECT password FROM admin WHERE email = %s"
            cursor.execute(query, (email,))
            result = cursor.fetchone()
            cursor.close()
        if result and check_password_hash(result[0], password):
            return True
        return False

    def get_user(self, email):
        with DatabaseConnection(*self.db_params) as conn:
            cursor = conn.cursor()
            query = "SELECT name, email FROM admin WHERE email = %s"
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
            query = "UPDATE admin SET name = %s, email = %s"
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
                logger.error("Error updating admin: %s", str(e))
                raise e
            finally:
                cursor.close()


#TO ADD THE ADMIN USER WE HAVE TO RUN THE BELOW LINES

# host = "localhost"
# database = "course_management"
# user = "user"
# password = "5001"
#
# run=Admin(host, database, user, password)
# name="vikas"
# email="vikas@gmail.com"
# password="1234"
# run.add_user(name, email, password)
# print("completed")