#  CONTROL FLOW IN PYTHON
#  Control flow refers to order in which statements are executed in aprogram.
#  instead of always running line, control flow allows your program to:
            
    # Make decisions (choose one path or another, explore alternatives).

    # Repeat actions (loops).

    # Exit or skip parts of code.

# A. Conditional Statements
# . if Statement
# Executes a block only when a condition is true.
age = 20 
if age >= 18:
    print("You are eligible to vote")

# some usecases
#  if-else
wallet = 400
price = 500

if wallet >= price:
    print("purchase successfull")
else:
    print("Insufficient balance")

# some usecases
# if-elif-else
score = 85
if score >= 70:
    print("grade A")
elif score >= 50:
    print("Grade B") 
else:
    print("Grade C")    

# Some usecases
# placing if in if 
age = 19
citizen = True

if age >= 18:
    if citizen:
        print("You can vote")
    else:
        print("You can vote")
else:
    print("Too young to vote ")


# B. Loops
# #1. for loop
# Iterates through each element in a LIST.
fruits = ["apple", "banana", "orange"]
for fruit in fruits: 
    print(f"I like {fruit}")


## Some usecases
# Iterating through shopping lists.

# Checking availability of products.

# Displaying student names, etc.



# Iterates through each element in a TUPLE.This Works like lists, but remember that tuples are immutable.

coordinates = (0.34654, -0.48585, 0.57477)
for point in coordinates:
    print(f"Point: {point}")

## Some usecases
# Storing fixed sensor readings.
# Displaying fixed seating positions, etc.


# Iterates through each element in a DICTIONARY. Remember that dictionaries have key-value pairs.

student = {"name": "Tunde", "age": 16, "grade": "A"}
for key, value in student.items():
    print(f"{key}: {value}")

# # Some usecases
# Reading database records.
# Showing user profile details.
# Checking configuration settings, etc.

# Iterates through each element in a STRING. Remember that strings are sequences of characters.

word = "PYTHON"
for char in word:
    print(char)

## Some usecases
# Counting vowels/consonants.
# Password validation (checking digits/special chars).
# Text analysis, etc.

# While loop


# Using while loop

## Documenting my thoughts##
# Let the loop start with count = 1
# Let it keep printing until count is greater than 5
# Let the loop terminate when the condition is no longer true

## My code
count = 1
while count <= 5:
    print("Number:", count)
    count += 1

# Incrementing with `while`

num = 1
while num <= 10:
    print(num, end=" ")
    num += 1

# Decrementing with `while`

timer = 10
while timer > 0:
    print("Countdown:", timer)
    timer -= 1

# While with User Input
## Keep asking until the user enters a correct password.

password = ""
while password != "python123":
    password = input("Enter the password: ")

print("Access Granted!")

#  Understanding while True

# while True:
    # Code block 
    # Must include a break statement to stop

# Keep asking the user for a name until they type "exit".

while True:
 name = input("Enter your name (type 'exit' to quit): ")
 if name.lower() == "exit":
        print("Goodbye!")
        break
 print(f"Hello, {name}")

# ---> I used `break` here. If you dont know what it is or what it is doing, its OK. I will explain it next...

## Useful in chat-like applications, forms, or data entry programs where users may input multiple times until they decide to stop.


# Loop control statements (break, continue and pass)
# 1. break
for num in range(1, 10):
    if num == 5:
        break
    print(num)

#   BREAK
#The loop stops completely when num == 5.
# Stop searching when an item is found.
# Exit when user input matches a condition.
# Prevent unnecessary iterations.

for num in range(1, 10):
    if num == 5:
        break
    print(num)


#   CONTINUE
#The loop stops completely when num == 5.
# Stop searching when an item is found.
# Exit when user input matches a condition.
# Prevent unnecessary iterations.

for num in range(1, 6):
    if num == 3:
        continue
    print(num)

# 3 is skipped , but the loop continues.
## some usecases
#  skip invalid data.
# ignore unwanted characters (like spaces in a string).
# continue running but avoid certain cases, etc.

#   PASS
for num in range(1, 6):
    if num == 3:
        pass
    else:
        print(num)

#  At num == 3, Python executes pass (nothing happens).

## Some usecases
#  Writing code structure (to fill in later).
# placeholders in class/method definitions.
#  Temporarily disable parts of code.

# lets try while True again

        #     TRY AND THINK THROUGH THIS.....
while True:
    print("\nMenu:")
    print("1. Say Hello")
    print("2. Say Goodbye")
    print("3. Exit")

    choice = input("choose an option: ")

    if choice == "1":
        print("Hello")
    elif choice == "2":
        print("Goodbye")
    elif choice == "3":
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Try again.")

# Try and use while True for validation

while True:
    age = input("Enter your age: ")
    if age.isdigit():
        print(f"Your age is {age}")
        break
    else:
        print("Invalid input. Please enter a number.")


# LEets make a guess

secret = "python"

while True:
    guess = input("Guess the secret word: ")
    if guess.lower() == secret:
        print("Correct! You guessed the word.")
        break
    else:
        print("Wrong! Try again.")



# Do you remember this?

balance = 10000000 

while True:
    print("\nATM Menu:")
    print("1. Check Balance")
    print("2. Withdraw")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print(f"Your balance is: {balance}")
    elif choice == "2":
        amount = int(input("Enter withdrawal amount: "))
        if amount <= balance:
            balance -= amount
            print(f"Withdrawal successful. New balance: {balance}")
        else:
            print("Insufficient funds.")
    elif choice == "3":
        print("Thank you for using our ATM. Goodbye!")
        break
    else:
        print("Invalid option. Try again.")
