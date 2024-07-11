#TASK1
course_name="CourseHub"
book_count=50

print("welcome to "+course_name+ "!")
print("Current book count is "+str(book_count))

book_name=input("Enter the book name: ")
print(book_name)

#TASK 9
#Step-1 Define course Information
course_name="CourseHub"
book_count=50

#step-2 Print Course Information
print("Welcome to " +course_name+ " !")
print("Current book count:" + str(book_count))

#step-3 Get user Input
book_name=input("Enter the Book Name: ")
print("You have entered: "+book_name)

#Step-4 Define Additional Variables
is_available=True

#step-5 Use Format Specifiers
output=f"The book'{book_name}'is currently {'available'if is_available else 'not available'}."
print(output)

#step-6 perform String Operations
author_name=input("Enter the Authour's Name: ")
concatenated_str=book_name+" by "+author_name
print("Concatenated String: "+concatenated_str)

#step-7 Use String Methods
print("Book name in lower case: "+book_name.lower())
print("Authour's name in upper case: "+author_name.upper())

#step-8 perform logical operators
has_python="python" in book_name
print("Does the book name contain 'python'?" +str(has_python))

#step-9 Convert Types
stock_str=input("Enter the stock input: ")
stock_int=int(stock_str)

#step-10 Display final output
final_message = (
    f"The book '{book_name}' by '{author_name}' is currently "
    f"{'available' if is_available else 'not available'} with {stock_int} copies in stock."
)
print(final_message)

#TASK 10
#Step 1: Open PyCharm and Navigate to the "coursehub" Project

#Step 2: Get Book price and calculate total value
price_per_book=float(input("Enter the price per book : "))
total_value=stock_int*price_per_book

#Step 3: Display final output
final_message = (f"The book '{book_name}' by {author_name} is currently "
                 f"{'available' if is_available else 'not available'} with {stock_int} copies in stock.\n"
                 f"The total value of the books in the library is ${total_value:.2f}.")
print(final_message)


#Step 4: Comparision operators
print("The book in stock = " +str(stock_int>0))

#Step 5: Logical operators
print("The book is available for borrowing "+str(stock_int >0 and is_available))

#Step 6: Assignment operators
stock_int +=10
print("Uptaded stock count after receiving new book :" +str(stock_int))

#Step 7: Bitwise operators
print("The stock count is even " +str(stock_int & 1==0))

                                       #TASK 11

course_titles=["Introduction to Python","Advanced Java","Web development with JavaScript","Data Structures in c++"]
course_instructors=("Mini","Smith","John","nick",)
print("Programming courses: ")
print(course_titles)
print("Course Instructors: ")
print(course_instructors)

#Using list methods
course_titles.append("Machine Learning Basics")  #Adding new course title
print("updated course titles: ")
print(course_titles)
course_titles.remove("Advanced Java")        #removing a course title
print("updated course titles after removal:")
print(course_titles)
course_titles.sort()                  #Sorting course titles
print("Sorted course titles: ")
print(course_titles)

#using tuple methods
instructor_index=course_instructors.index("Mini")  #Finding the index of a course instructor
print("Index of Mini:", instructor_index)

instructor_count = course_instructors.count("John")
print("Number of times John  appears:", instructor_count)


#day 12
#TASk1
courses= [
    {"course_name": "Python Programming", "book_count": 30, "is_available": True},
    {"course_name": "Data Structures", "book_count": 20, "is_available": False},
    {"course_name": "Web Development", "book_count": 15, "is_available": True},
    {"course_name": "Machine Learning", "book_count": 25, "is_available": True}
]
print(courses)

unique_course_names = set()
course_details = {}
course = courses[0]
unique_course_names.add(course["course_name"])
course_details[course["course_name"]] = {
    "book_count": course["book_count"],
    "is_available": course["is_available"]
}

course = courses[1]
unique_course_names.add(course["course_name"])
course_details[course["course_name"]] = {
    "book_count": course["book_count"],
    "is_available": course["is_available"]
}

course = courses[2]
unique_course_names.add(course["course_name"])
course_details[course["course_name"]] = {
    "book_count": course["book_count"],
    "is_available": course["is_available"]
}

course = courses[3]
unique_course_names.add(course["course_name"])
course_details[course["course_name"]] = {
    "book_count": course["book_count"],
    "is_available": course["is_available"]
}

print("Unique Courses and Their Details:")
course_name = "Python Programming"
details = course_details[course_name]
print(f"Course Name: {course_name}")
print(f"Book Count: {details['book_count']}")
print(f"Availability: {'Available' if details['is_available'] else 'Not Available'}")
print()

# Display details for the second course
course_name = "Data Structures"
details = course_details[course_name]
print(f"Course Name: {course_name}")
print(f"Book Count: {details['book_count']}")
print(f"Availability: {'Available' if details['is_available'] else 'Not Available'}")
print()

# Display details for the third course
course_name = "Web Development"
details = course_details[course_name]
print(f"Course Name: {course_name}")
print(f"Book Count: {details['book_count']}")
print(f"Availability: {'Available' if details['is_available'] else 'Not Available'}")
print()

# Display details for the fourth course
course_name = "Machine Learning"
details = course_details[course_name]
print(f"Course Name: {course_name}")
print(f"Book Count: {details['book_count']}")
print(f"Availability: {'Available' if details['is_available'] else 'Not Available'}")
print()

#day 13
#TASK
course_name="CourseHub"
book_count=50
print("Welcome to " + course_name + "!")
print("Current book count: " + str(book_count))
book_name = input("Enter the book name: ")
print("You have entered: " + book_name)
author_name = input("Enter the author's name: ")
concatenated_str = book_name + " by " + author_name
print("Concatenated String: " + concatenated_str)
print("Book name in lowercase: " + book_name.lower())
print("Author name in uppercase: " + author_name.upper())
stock_str = input("Enter the stock quantity: ")
stock_int = int(stock_str)

#Using conditional statements
if stock_int>0:
    print(f"The book '{book_name}' by {author_name} is available with {stock_int} copies in stock.")
else:
    print(f"The book '{book_name}'by {author_name} is not available as it is out of stock")

#Task 14
def add_course(courses):
     course_name=input("Enter the course name: ")
     book_count=int(input("Enter the number of books: "))
     is_available=input("Is the course available? yes/No: ").strip().lower()=='Yes'
     new_course={
         "course_name":course_name,
         "book_count":book_count,
         "is_available":is_available
     }
     courses.append(new_course)
     print(f"Course '{course_name}' has been uploaded successfully")

     def display_courses(courses):
         if not courses:
             print("No courses available")
             return
         for course in courses:
             course_name=course["course_name"]
             book_count=course["book_count"]
             is_available=course["is_available"]
             print(f"Course Name:{course_name}")
             print(f"Book Count:{book_count}")
             print(f"Availability: {'Available' if is_available else 'not available'}")
             print()
         def manage_course_inventory(courses):
             course_name=input("Enter the course name to update: ")
             for course in courses:
                 if course["course_name"].lower()==course_name.lower():
                     new_book_count=int(input(f"Enter the book_count for {course_name}:"))
                     course["book_count"] = new_book_count
                     print(f"Book count for '{course_name}' has been updated to {new_book_count}.")
                     return
                 print(f"course '{course_name}' is not found")
             while True:
                print("\n CourseHub Management System")
                print("1. Add a Course")
                print("2. Display Courses")
                print("3. Manage Course Inventory")
                print("4. Exit")
                choice = input("Enter your choice (1-4): ")
                if choice == '1':
                    add_course(courses)
                elif choice == '2':
                    display_courses(courses)
                elif choice == '3':
                    manage_course_inventory(courses)
                elif choice == '4':
                    print("Exiting the system. Goodbye!")
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and 4.")


#lambda Functions
courses=[
    {"course name":"Python Programming", "Book_count": 50, "is_ available":True,"price":200}
    {"course name":"Java programming","Book count":20, "is_available":True,"price":500},
    {"course name":"Machine Learning", "Book_count": 150, "is_ available":False,"price":200}
    {"course name":"Data Science", "Book_count": 500, "is_ available":True,"price":200}
]
sorted_courses_by_price=sorted(courses, key=lambda x:x['price'])
minimum_book_count=20
filtered_courses_by_quantity=list(filter(lambda x:x ))

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


#step 2 Database connection parameters

import psycopg2
host="localhost",
database="new_db",
user="manasa",
password="1234"
conn=psycopg2.connect(
    host=host,
    database=database,
    user=user,
    password=password
)
cursor=connection.cursor
print("Connected to the database successfully.")

#step 3 creating a course table
create_table_query ="""
CREATE TABLE courses (
    course_id SERIAL PRIMARY KEY,
    course_name VARCHAR(255) NOT NULL,
    instructor VARCHAR(255) NOT NULL,
    duration INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL
);"""
cursor.execute(create_table_query)
connection.commit()
print("Course table created successfully.")

#step 4 Insert values into the course table
def insert_course(course_name,instructor,duration,price):
    insert_query =
        INSERT INTO courses (course_name, instructor, duration, price)
        VALUES (%s, %s, %s, %s);

    cursor.execute(insert_query, (course_name, instructor, duration, price))
    connection.commit()
    print(f"Course '{course_name}' inserted successfully.")


#step 5 modifying the course table
def update_course(course_id, course_name=None, instructor=None, duration=None, price=None):
    update_query = "UPDATE courses SET "
    update_values = []
    if course_name:
        update_query += "course_name = %s, "
        update_values.append(course_name)
    if instructor:
        update_query += "instructor = %s, "
        update_values.append(instructor)
    if duration:
        update_query += "duration = %s, "
        update_values.append(duration)
    if price:
        update_query += "price = %s, "
        update_values.append(price)
    update_query=update_query.rstrip(", ") + " WHERE course_id = %s;"
    update_values.append(course_id)
    cursor.execute(update_query, tuple(update_values))
    connection.commit()
    print(f"Course with ID '{course_id}' updated successfully.")

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

