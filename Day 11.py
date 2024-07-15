


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


