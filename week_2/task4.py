# Task 1
quote =input("please input your favourite quote: ")
quotes = quote.title()
print(f"\"{quotes}\"")

# Task 2
shopping_list = []
for i in range (3) :
    item = input(f"Enter shopping item {i+1}: ")
    shopping_list.append(item)
    print(", ".join(shopping_list))

# Task 3
users_sentence = input("enter users sentence")
word = users_sentence.split()
word_count = len(word)
print(f"your senstenceconsist of {word_count}wors. ")

# Task 4 
print("Task 4: Name Organize \n")
print("A: Ask the user to 5 names (seperated by spaces). \n")
name1 =("enter five names seperated by spaces: ")
print(name1)

print("B: Convert all names to lowercase. \n")
print(name1.lower())

print("C: Sort the list alphabetically. \n")
list1 = name1.split()
list1.sort()

print("D: Display them one name per line. Tips: use'range()', 'sort()', 'for', 'in' 'split'(), 'len()', 'lower()' \n")
print("\nsorted names:")
for name1 in list1:
    print(name1)

# Task 5
name = [] 
score =  []
student_1 = input("input the first student name")
name.append(student_1)
student_2 = input("input the second student name")
name.append(student_2)
student_3 = input("input the third student name")
name.append(student_3)
student_score1 = input("input the score for student_1")
score.append(student_score1)
student_score2 = input("input the score for student_2")
score.append(student_score2)
student_score3 = input("input the score for student_3")
score.append(student_score3)
result = name + score
print(result)



# Task 6
word = input("enter a word")
print(len(word))
is_upper = word.isupper()
is_lower = word.islower()
title = word.istitle()
reverse_word = word[::-1]
print(reverse_word)

# Task 7
cities = ["Lagos", "Ogun", "Osun", "Ibadan", "Jos"]
new_third_city = input("Enter a new city to replace the third city: ")
cities[2] = new_third_city
cities.pop()
new_first_city = input("Enter a new city to add at the beginning: ")
cities.insert(0, new_first_city)
print("Updated list of cities:", cities)

