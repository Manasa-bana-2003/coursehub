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
    f"The book '{book_name}' by {author_name} is currently "
    f"{'available' if is_available else 'not available'} with {stock_int} copies in stock."
)
print(final_message)

