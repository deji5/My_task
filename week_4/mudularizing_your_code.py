# See Examples of use here
#  range()
for i in range(3):
    print(i)    #0, 1,2

# zip()
names = ["Eshter","Precious","kennie"]
scores = [85, 90, 75]
for n, s in zip(names, scores):
    print(n, "Scored", s)

# It's ok, if dont know lamba is or how to use it . I will touch on it later. Just focus on the outputs
# map()
nums = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, nums))
print(squared)  # [1, 4, 9, 16]

#  filter()
even_nums = list(filter(lambda x: x % 2 == 0, nums))
print(even_nums)  # [2, 4]

#  Student Performance & Feedback System

#  Step 1: Input student data
name1 = input("Enter first student name: ")
score1 = int(input("Enter score for " + name1 + ": "))

name2 = input("Enter second student name: ")
score2 = int(input("Enter score for " + name2 + ":"))

name3 = input("Enter second student name: ")
score3  = int(input("Enter score for " + name3 + ":"))

#  step 2: Store in list
names = [name1, name2, name3]
scores = [score1, score2, score3]

#  step 3: Display data 
print("\nStudent Data:")
for index, (n, s) in enumerate(zip(names, scores)):
    print(f"{index + 1}. {n} - {s}")

# step 4: summary using built-ins
total = sum(scores)
average = round(total / len(scores), 2)
highest = max(scores)
lowest = min(scores)

print("\nperformance summary: ")
print("Total Score:", total)
print("Average score:", average)
print("Highest score:", highest)
print("Lowest Score:", lowest)

# Step 5: Ranking (using sorted and zip)
ranked = sorted(zip(scores, names), reverse=True)
print("\nRanking:")
for rank, (score, name) in enumerate(ranked, 1):
    print(f"{rank}. {name} - {score}")

# Step 6: Check data types
print("\nData Type Checks:")
print("Type of names:", type(names))
print("Type of scores:", type(scores))
print("ID of names list:", id(names))
print("ID of scores list:", id(scores))

# Step 7: Filter passing students (>=50)
passing = list(filter(lambda s: s >= 50, scores))
print("\nPassing Scores:", passing)

# Step 8: Map names to uppercase
upper_names = list(map(lambda n: n.upper(), names))
print("Uppercase Names:", upper_names)

# Step 9: Use help() to show documentation of len
print("\nHelp on len():")
help(len)


# I just made use of most of the built-in functions. You can write your own version of this code. Just think through it

#  Defining afunction
def greet():
    print("Hello, welcome to AI Fellowship!")

# When you want to use a function, this is how to call it.
#  And you can call it as many times as possible.
greet()
greet()
greet()
 
#  Function with an argument - the placeholder
def greet(name):
    print("Hello", name, "welcome to python learning!")

# Calling with parameter- the actual name
greet("class rep")
greet ("Ridwan")

def  greet(name):
    print("Hello", name)

#  Function call
result = greet("Esther")

# you will notice it not store the name
print("Result:" , result)

def add(a, b):
    return a +b
# funtion call

result = add(4, 6)
print("The sum is:", result)

#  Note the output and compare it with that of print()

##  Postion arguments
def introduce(name, track):
    print("My name is :", name)
    print("I am learning", track)

# function call
introduce("Ngozi", "AI Engineering")   # Correct order

# Chage the arrangement and watch the output
# introduce("AI Engineering", "Ngozi")     Incorrect order, this will throw a semantic error

# # Keyword Arguments
def introduce(name, track):
    print("My name is :", name)
    print("I am learning", track, ".")

#  function call
introduce(name = "Ngozi", track = "AI Engineering")

# Change the arrangement and watch the output
introduce(track =  "AI Engineering",name = "Ngozi")  #Here yoy notice that oder does not batter

## Default Arguments
def introduce(name, track = "AI Engineering"):
    print("My name is", name)
    print("i am learning", track+".")

# function call

#  with specify the default argument , but watch the output
introduce("Paul")

# Specify the defaukt argument and watch the output
introduce("Tunji Pual", track = "AI Development")

# VARYING LENGTH ARGUMENTS
## non-keyword(tuple)
def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    print("Sum:", total)

#  function call
#  take note of the output 
add_numbers(2, 4, 6)
add_numbers(10, 20, 30, 40, 50)

# keyword argument(dictionary)
def student_details(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

#  function call - Take note of the output
student_details(name="Peter", track = "AI Engineering", interest="block chain")

# Define student profile function

# Ensure to not the order of arrangement of the types of arguments used.
# This is how to arrange it of you are using everything or some of the together

# # Lets implement on full code
# Define stuent profile function

#  Ensure to not the order of arrangement of the types of arguments used.
# This is how to arrange it of you are using everythng or some of the together

def participant_profile(name, age, track="AI Development", *skills, **extra_info):
    """
    Generate a profile for a bootcamp participant using different types of arguments.
    """
    profile = f"\n--- Bootcamp Participant Profile ---\n"
    profile += f"Name: {name}\n"
    profile += f"Age: {age}\n"
    profile += f"Track: {track}\n"

    # Skills (from *args)
    if skills:
        profile += "Skills: " + ", ".join(skills) + "\n"
    else:
        profile += "Skills: Not yet specified\n"

    # Extra info (from **kwargs)
    if extra_info:
        profile += "Additional Info:\n"
        for key, value in extra_info.items():
            profile += f" - {key.capitalize()}: {value}\n"

    return profile  # Do you remember `return` and why it is used? We are using it so it can be reused in other places


# ----------Lets test -----------
# Example 1: Using only positional arguments
print(participant_profile("peter", 24))

# Example 2: adding keyword/default arguments
print(participant_profile("+Ridwan", 29, track="AI Engineering"))

# Example 3: Adding variable-length positional arguments (*args)
print(participant_profile("David", 27, "Data Science", "Python", "SQL", "Machine Learning"))

# Example 4: Adding variable-length keyword arguments (**kwargs)
print(participant_profile(
    "Sophia", 30, "Cybersecurity",
    "Networking", "Ethical Hacking", "Python",
    interest="Blockchain", city="Shagamu", phone="08123456789"
))

#Namespaces and Scope
# Global Namespace
employee = "General Employee"  

def IT_department():
    # Local Namespace inside IT_department
    employee = "Chris (IT)"
    print("Inside IT Department:", employee)

def Training_department():
    # Local Namespace inside Training_department
    employee = "Chris (Training)"
    print("Inside Training Department:", employee)

print("In Global Namespace:", employee)  # Refers to global variable

IT_department()   # Uses local variable in IT
Training_department()   # Uses local variable in Training

# Using a built-in namespace function
print("Length of 'Python':", len("Python"))  

# So 'Chris' can exist in more than one namespace without conflict.
# Please, take your time to study the output carefully.

# Scope
x = "global x"   # Global Namespace

def outer():
    x = "enclosing x"  # Enclosing Namespace
    
    def inner():
        x = "local x"  # Local Namespace
        print("Inside inner:", x)  # Local wins
    
    inner()
    print("Inside outer:", x)  # Enclosing
    
outer()
print("In global:", x)  # Global

# Watch the output
# Notice how Python searches in the order Local → Enclosing → Global → Built-in (LEGB).


### Global keyword

# Used when you want to modify a global variable inside a function.

x = 5

def change_global():
    global x
    x = 10   # modifies the global x

change_global()
print(x)  # Output: 10

# Watch the output



# nonlocal keyword

#Used in nested functions when you want to modify the variable from the enclosing scope (not global).

def outer():
    x = "outer x"
    
    def inner():
        nonlocal x
        x = "changed by inner"
        print("Inside inner:", x)
    
    inner()
    print("Inside outer:", x)

outer()

# Watch the output



# Normal function
def square(x):
    return x ** 2

# Lambda function
square_lambda = lambda x: x ** 2

print(square(5))         
print(square_lambda(5))  

# Watch the output and note the difference



# This one has more that one arguments.

add = lambda a, b: a + b
print(add(3, 7))  # Output: 10



# Let us lambda to apply the square function to a list

numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x**2, numbers))
print(squares)  # Output: [1, 4, 9, 16]



# Lets use lambda to filter even numbers 

numbers = [10, 15, 20, 25, 30]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # Output: [10, 20, 30]



# Lets use lambda to sort the tuple within a list.

students = [("Ayo", 20), ("Bola", 18), ("Chika", 22)]
# Sort by age
sorted_students = sorted(students, key=lambda student: student[1])
print(sorted_students)

  
# Output: [('Bola', 18), ('Ayo', 20), ('Chika', 22)]

students_sorted_descending = sorted(students, key=lambda student: student[1], reverse=True)
print(students_sorted_descending)

# Output: [('Chika', 22), ('Ayo', 20), ('Bola', 18)]

students_sorted_alphabetically = sorted(students, key=lambda student: student[0])
print(students_sorted_alphabetically)

# Output: [('Ayo', 20), ('Bola', 18), ('Chika', 22)]