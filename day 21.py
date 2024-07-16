import logging
import psycopg2
from psycopg2 import sql
from werkzeug.security import check_password_hash, generate_password_hash

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
            database=self.database,  # Fixed typo here
            user=self.user,
            password=self.password
        )
        return self.connection

    def __exit__(self, exc_type, exc_val, traceback):
        if self.connection:
            self.connection.close()
        if exc_type is not None:
            logger.error("Exception occurred: %s", exc_val)
        logger.info("Database connection closed.")

class Course:
    def __init__(self, id, name, desc, author, availability, edition, count):
        self.id = id
        self.name = name
        self.desc = desc
        self.author = author
        self.availability = bool(availability)
        self.edition = edition
        self.count = count

    def __str__(self):
        return (f"Course ID: {self.id}, Name: {self.name}, Description: {self.desc[:60]}..., "
                f"Author: {self.author}, Available: {self.availability}, Edition: {self.edition}, Count: {self.count}")

def fetch_courses(connection):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM courses")
        courses_data = cursor.fetchall()
        courses = [Course(*data) for data in courses_data]
    return courses

# Usage example
host = "localhost"
database = "new_db"
user = "manasa"
password = "1234"

with DatabaseConnection(host, database, user, password) as connection:
    courses = fetch_courses(connection)
    for course in courses:
        print(course)
