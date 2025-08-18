store = {"Book": 10, "Pen": 20, "Bag": 30}
interest = input(f"the folllowing items are avaliable {store}, what like to buy: ").title()
quantity =int(input(f"How many {interest}s would you like to buy: "))
store[interest] -= quantity
print(store)