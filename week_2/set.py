# Set in python

# creating set

# 1. Using curly braces
fruits = {"apple", "banana", "mango"}
print(fruits)

# 2. Using the set() constructor
numbers = set([1, 2, 3, 4])
print(numbers)

# 3. creating an empty set (must use set(), not {})
empty_set = set()
print(empty_set)

# 4. From a string (duplicate removed automatically)
letters = set("mississippi")
print(letters)

# Set operation
# Adding Elements 
colours = {"red", "blue"}
colours.add("greeen")
print(colours)

# Removing elements
colours.remove("blue") # removes an elements, raises error if not found
colours.discard("yellow") # removes if found, no error if missing
print(colours)

# Pop an element
colours = {"red", "blue", "green"}
removed = colours.pop()
print("Removed:", removed)
print("rReemaining", colours)

