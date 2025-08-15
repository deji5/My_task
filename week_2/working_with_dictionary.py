# Working with Dictionary
# dictionary_name = {Key1: value1, key2: value2}
# 1. Using curly braces
student = {
    "name": "Ada",
    "age": 20,
    "course": "Computer Science"
}
print(student)

# 2. Using the dict() constructor
student_info = dict(name="John", age=25, course="Maths")
print(student_info)

# 3. Empthy Dictionary
empty_dict = {}
print(empty_dict)

#Dictionary Comprehension
# syntax
# {key_expression:value_expression for item in iterable if condition}
# Create a dictionary of numbers and their squares
squares = {x:x**2 for x in range(1, 6)}
print(squares)

# With Condition
# Dictionary of even numbers and their cubes
evens_cube = {x: x**3 for x in range(1, 10) if x % 2 == 0}
print(evens_cube)

# From Existing Dictionary
student = {"Ada": 85, "John": 40, "Musa": 65}
# Filter students who pssed(score >= 50)
Passed_student = {name: score for name, score in student.items() if score >=50}
print(Passed_student)

# Using String Keys
names = ["Ada", "John", "Moses"]
lenghts = {name: len(name) for name in names}
print(lenghts)

# Accessing Dictionary Items
# Define a dictionary
student = {"name": "Ada", "age": 20, "Course": "Computer science"}

# using keys
print(student["name"])

# Using get() method (avoid error if key is missing)
print(student.get("age"))
print(student.get("grade", "Not Found"))

student["age"] = 21  # Change value
student["grade"] = "A"  # Add new key-value pair
print(student)

# 1. Using pop()
student.pop("grade")
print(student)
# 2. Using popitem() - removes last inserted key-value
student.popitem()
print(student)
# 3. Using del keyword
del student["course"]
print(student)
# 4. Using clear() - removes all items
student.clear()

print(student)

person = {"name": "Emeka", "age": 30}

# 1. keys()
print(person.keys())

# 2. values()
print(person.values())

# 3. items()
print(person.items())

# 4. update()
person.update({"age": 31, "city": "Lagos"})
print(person)

# NESTED DICTIONARY
students = {
    "student1": {"name": "Ada", "age": 20 },
    "student2": {"name": "Jonh", "age": 22}
}

print(students["student1"]["name"]) # Access nested data

# DEFINE A DICTIONARY
student = {"name": "Ada", "age": 20, "course": "Computer Science"}

# loop through keys
for key in student:
    print(key)

# Loop through values
for value in student.values():
    print(F"{key}: {value}")

# Storing ba student's biodata
student = {
    "name": "chinedu",
    "age": 19,
    "deparment": "Engineering",
    "subjects": ["Maths", "Physics", "Chemistry"],
    "is_full_time": True
}

print(f"Name: {student['name']}")
print(f"Subject: {','.join(student['subjects'])}")