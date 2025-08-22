voters = set()
while True:
    try:
        name = input("enter voters names: ").title()
        if name.lower()== 'done':
            break
        if name in voters:
            print(f"warning '{name}' already exist")
        else:
            voters.add(name)
            print(f"this {name} as  been registered.")
    except ValueError as a:
        print("Error:", a)
    except Exception as f:
        print("Unexpected Error:", f)
print("\nRegistration succefull!")
print(f"Total unique voters:{len(voters)}") 
