#LISTS
#Creating a list
fruits=["Apple","Banana","Cherry"]

#accessing items
print(fruits[0])
print(fruits[1])
print(fruits[2])

#Modifying a list
fruits[1]="Pineapple"
print(fruits)

#List methods
#1 append
fruits.append("Orange")
print(fruits)

#2 insert
fruits.insert(3,"Mango")
print(fruits)

#3 remove
fruits.remove("Apple")
print(fruits)

#4 pop
fruits.pop(1)
print(fruits)

#5 sort
fruits.sort()
print(fruits)

#6 reverse
fruits.reverse()
print(fruits)

#7 len
print(len(fruits))

#8 clear
fruits.clear()
print(fruits)

#TUPLES
#Creating a tuple
fruits=("Apple","Banana","Cherry","Dragon Fruit")
print(fruits)

#Accessing an element
print(fruits[0])
print(fruits[1])
print(fruits[2])

#Tuple methods
#1 count
print(fruits.count("Apple"))

#2 index
print(fruits.index("Dragon Fruit"))


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


