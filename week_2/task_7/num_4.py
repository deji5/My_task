name1 = input("enter 3 your: ").split()
convertname = set(name1)
name = {name1: len(name1) for name1 in convertname}
print(name)
