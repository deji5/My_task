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
print("i am a boy")