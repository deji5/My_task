# Task 1
dishes = ()
dish1 = input("enter first favourite dish")
dish2 = input("enter second favourite dish")
dish3 = input("enter third favourite dish")

dishes = dish1, dish2, dish3
print(dishes)
print(*dishes, sep="\n")


# Task 2
friend = input("Enter 5 of yyour best friend names putting in spaces: ").split()
friends = tuple(friend)
print(type(friends))
print(friends[::-1])


# Task 3
state = input("enter state: ").title().split()
print(state[:0], state[:-1])
print("Lagos" in state)
print(len(state))

# Task 4
first_name = input("enter first name")
age = input("input age")
favourite_colour =input("enter your favourite colour")
home_town = input("enter your home town")
escape = tuple(input(f"name:\t{first_name}\nAge:\t{age}\ncolour:\t{favourite_colour}\ntown\t{home_town}"))
# information = tuple([first_name] + [age] + [favourite_colour] + [home_town])
print(escape)

# Task 5
shop = input("enter shopping list item").split()
shopping_list = tuple(shop)
listshop = list(shopping_list)
listshop.extend(["garri", "ferrero"])
print(listshop)
shopping_tuple =tuple(listshop)
print("|".join(shopping_tuple))

Task 6
weeks = ("monday", "tuesday", "wednessday", "thursday", "friday", "saturday", "sunday")
print(type(weeks))
name = input("enter student name")
gender = input("enter your gender")
course_track = input("enter your course track: ")
current_month = input("enter current month using numbers: ")
current_day = input("enter todays date")

weeks = tuple(current_day)
month = tuple(current_month)
print(weeks)