import psycopg2
#create database handler class
class DatabaseHandler:
    def __init__(self,host,database,user,password):
        self.host=host
        self.database=database
        self.user=user
        self.password=password
        self.connection=None
        self.cursor=None
#connect to databse
    def connect(self):
        self.connection=psycopg2.connect(host=self.host,database=self.database,user=self.user,password=self.password)
        self.cursor=self.connection.cursor()
#Execute queries
    def execute_query(self,query):
        self.cursor.execute(query)
        return self.cursor.fetchall()
#close connection
    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
class Book:
    def __init__(self, id, name, desc, author, availability, edition, count):
        self.id = id
        self.name = name
        self.desc = desc
        self.author = author
        self.availability = bool(availability)
        self.edition = edition
        self.count = count

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Description: {self.desc[:60]}..., Author: {self.author}, Available: {self.availability}, Edition: {self.edition}, Count: {self.count}"
class BookDBHandler(DatabaseHandler):
    def fetch_books(self):
        self.connect()
        books_data = self.execute_query("SELECT * FROM books")
        books = []
        for book_data in books_data:
            book = Book(*book_data)
            books.append(book)
        self.close()
        return books

host = "localhost"
database = "new_db"
user = "manasa"
password = "1234"

book_handler = BookDBHandler(host, database, user, password)
books = book_handler.fetch_books()

for book in books:
    print(book)
