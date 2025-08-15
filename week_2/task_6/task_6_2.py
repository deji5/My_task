names = set()
num_names = int(input("how many names: "))
for _ in range(num_names):
    name = input("Enter a name: ")
    names.add(name)
print("Names in alphabetical order: ")
print(sorted(names)) 