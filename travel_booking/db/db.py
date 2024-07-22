import logging
import psycopg2
from psycopg2 import sql
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

    def __exit__(self, exc_type, exc_val, traceback):
        if self.connection:
            self.connection.close()
        if exc_type is not None:
            logger.error("Exception occurred: %s", exc_val)
        logger.info("Database connection closed.")

class Place:
    def __init__(self, id, name, description, location, rating):
        self.id = id
        self.name = name
        self.description = description
        self.location = location
        self.rating = rating

    def __str__(self):
        return (f"Place ID: {self.id}, Name: {self.name}, Description: {self.description[:60]}..., "
                f"Location: {self.location}, Rating: {self.rating}")

class Places:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password

    def fetch_places(self, search_term):
        with DatabaseConnection(self.host, self.database, self.user, self.password) as connection:
            with connection.cursor() as cursor:
                query = sql.SQL("SELECT * FROM place WHERE name ILIKE %s")
                cursor.execute(query, (f"%{search_term}%",))
                places_data = cursor.fetchall()
                places = [Place(*data) for data in places_data]
        return places