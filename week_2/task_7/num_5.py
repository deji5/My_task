names = input("enter 3 names: ").split()
name = set(names)
phone_num = (input("enter phone number")).split()
# phone_nums = set(phone_num)
combination = {names:phone_num for names,
               phone_num in zip(names, phone_num)}
print(combination)