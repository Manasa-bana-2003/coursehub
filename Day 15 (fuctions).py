#basic structure of a function
def Function_name(parameters):
    return result

#keyword arguments
def add_numbers(a,b):
    return a+b
result=add_numbers(a=3,b=7)
print(result)

#arbitrary arguments
def greet(*names):
    for name in names:
        print(f"Hello,{name}!")
    greet("Alice", "Bob", "Charlie")

#Documentation strings
def add_numbers(a,b):
    return a+b
print(add_numbers.__doc__)


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


