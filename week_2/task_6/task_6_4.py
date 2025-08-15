voters = set()
while True:
    name = input("enter voters names: ").strip()
    if name.lower()== 'done':break
    if name in voters:
        print(f"warning '{name}' already exist")
    else:
        voters.add(name)
        print(f"this {name} as  been registered.")
print("\nRegistration succefull!")
print(f"Total unique voters:{len(voters)}")            