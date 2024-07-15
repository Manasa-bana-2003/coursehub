'''class Car:
    def __init__(self,color,model,year):
        self.color=color
        self.model=model
        self.year=year
    def start_engine(self):
        print("Engine Started")
    def stop_engine(self):
        print("Engine Stopped")
#Creating an object of class car
my_car=Car("Red","Toyota",2020)
print(my_car.color)
my_car.start_engine()

#special methods(__init__ and __str__)
class Car:
    def __init__(self,color,model,year):
        self.color=color
        self.model=model
        self.year=year
    def __str__(self):
        return f"Car Details - color:{self.color},model:{self.model},year:{self.year}"
#creating an object of class car
my_car=Car("Red","Toyota",2020)
print(my_car)

#Understanding the self parameter
class Car:
    def __init__(self,color,model,year):
        self.color=color
        self.model=model
        self.year=year
    def display_details(self):
        print(f"Color: {self.color}, Model: {self.model}, Year: {self.year}")
#creating objects of class car
car1=Car("Red","Audi",2014)
car2=Car("Black","Toyota",2021)
car1.display_details()
car2.display_details()'''


#defining a python class for book management

class Book:
    def __init__ (self,id,name,desc,author,availability,edition,count):
        self.id=id
        self.name=name
        self.desc=desc
        self.author=author
        self.availability=bool(availability)
        self.edition=edition
        self.count=count
    def __str__(self):
        return f"ID:{self.id},Name:{self.name},Description:{self.desc[:60]}...,Author:{self.author},Available:{self.availability},Edition:{self.edition},Count:{self.count}"


#connecting to the postgre sql database

import psycopg2
host="localhost"
database="new_db"
user="manasa"
password="1234"
connection = psycopg2.connect(
    host=host,
    database=database,
    user=user,
    password=password
)
cursor=connection.cursor()

# Function to fetch books from the database
def fetch_books():
    cursor.execute("SELECT * FROM books")
    books_data = cursor.fetchall()
    books = []
    for book_data in books_data:
        book = Book(*book_data)
        books.append(book)
    return books

# Fetch books from the database
books = fetch_books()

# Iterate over the fetched books and print their details
for book in books:
    print(book)

cursor.close()
connection.close()
print("Database connection closed.")

