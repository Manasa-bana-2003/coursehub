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
print("The stock count is even " +str(stock_int & 1==0) )