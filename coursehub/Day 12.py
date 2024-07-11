#SETS

#creating a set
my_set={1,2,3,4,5,6}        #using curly braces{}
my_set=set([1,2,3,4,5,6,7]) #using set()
print(my_set)

#SET OPERATIONS
#1.union
set1={1,8,5,9,4,2,5,7}
set2={9,6,7,8,0,2,1,5}
union_set=set1.union(set2)
print(union_set)

#2. intersection
set1={1,8,5,9,4,2,5,7}
set2={9,6,7,8,0,2,1,5}
intersection_set=set1.intersection(set2)
print(intersection_set)

#3. difference
set1={1,8,5,9,4,2,5,7}
set2={9,6,7,8,0,2,1,5}
difference_set1=set2.difference(set1)
print(difference_set1)
difference_set2=set1.difference(set2)
print(difference_set2)

#4. Symmetric difference
set1={1,8,5,9,4,2,5,7}
set2={9,6,7,8,0,2,1,5}
sd_set=set1.symmetric_difference(set2)
print(sd_set)

#other methods
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)

my_set.remove(2)
print(my_set)

my_set.discard(3)
print(my_set)

my_set.clear()
print(my_set)


#DICTIONARIES
#creating a dictionary
my_dict1= {'name': 'Alice', 'age': 25, 'city': 'New York'}
my_dict=dict(name= 'Alice', age= 25, city='New York')
print(my_dict1)
print(my_dict)

#Accessing an element
my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}
print(my_dict['name'])
print(my_dict.get('age'))

#Adding and updating
my_dict = {'name': 'Alice', 'age': 25}
my_dict['city'] = 'New York'
my_dict['age'] = 26
print(my_dict)

#Removing elements
my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}
my_dict.pop('age')
print(my_dict)

del my_dict['city']
print(my_dict)

my_dict.popitem()
print(my_dict)


#other methods
my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())

my_dict.clear()
print(my_dict)


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