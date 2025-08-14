# Using parentheses()
# Exanple 1: tuple with multiple items
fruits = ("apple", "banana", "cherry")
print(fruits)  #('apple', 'banana', 'cherry')

# pwithout parentheses
numbers = 1,2,3
print(numbers) # (1, 2, 3)

single_item = ("apple",)
print(single_item)      # ('apple',)
print(type(single_item))# <class 'tuple'>

# Using the tulpe() contructor
fruits_list = ["apple", "banana", "cherry"]
fruits_tuple = tuple(fruits_list)
print(fruits_tuple) #('apple', 'banana', 'cherry')

#Ordered
colors = ("red", "green", "blue")
print(colors[0])  # red

# Immutable ( uncomment and run. This will cause an error)
# colours[1] = "yellow" # TypeError

# Allow duplicates
numbers = (1, 2, 2, 3)
print (numbers)  # (1, 2, 2, 3)

# Mixed data types
mixed = ("apple", 3, True, 5.6)
print(mixed)     # ('apple', 3, True, 5.6)


# 1. Indexing
fruits = ("apple", "banana", "cherry")
print(fruits[1])     # banana 
print(fruits[-1])    # cherry

# 2. Slicing

print(fruits[0:2])   # ('apple', 'banana')
print(fruits[::-1])  # ('cherry', banana', 'apple')

# 3: concatenation
tuple1 = (1, 2)
tuple2 = (3, 4)
result = tuple1 + tuple2
print(result)   # (1, 2, 3, 4)

# 4. Repetition
nums = (1, 2)
print(nums * 3) # (1, 2, 1, 2, 1, 2)

# 5. Membership
fruits = ("apple", "banana", "cherry")
print("banana" in fruits)   # True
print("grape" not in fruits)# True

# 6. Iteration
for fruit in fruits: 
    print(fruit)


# Unpacking tuples

#tuples have only two maethods

# dont count() and dot index()

numbers = (1, 2, 3, 4)

print(numbers.count(2))  # 2 (count occurrences of 2)
print(numbers.index(3))  # 3 (position of first occurrences of 3)

# Tuple of List
t = (1, 2, 3)
lst = list(t)
lst.append(4)
print(lst)   # [1, 2, 3, 4]

# List back to tuples
t = tuple(lst)
print(t)    # (1, 2, 3, 4)
 
nums = (4, 1, 7, 3)
print(len(nums))   #4   # len means lenght
print(max(nums))   #7   # max means biggest number
print(min(nums))   #1   # min means smallest number
print(sum(nums))   #15  # sum means add up all numbers

person = ("John", 25, "Nigeria")
name,age,country = person
print(name)      #John 
print(age)       #25
print(country)   #Nigeria
