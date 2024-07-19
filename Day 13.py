#Conditional statements
#if statements
age=20
if age>=18:
    print("you are an Adult")

#if and else
age=9
if age>=18:
    print("You are an Adult")
else:
    print("You are not an adult")


#if, else and elif
age=int(input("Enter the age: "))
if age<13:
    print("You are a Child")
elif age<18:
    print("You are a teenager")
else:
    print("You are an Adult")


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
    print("The book '{book_name}'by {author_name} is not available as it is out of stock")
