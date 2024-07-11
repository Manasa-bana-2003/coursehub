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



