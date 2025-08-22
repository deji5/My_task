name = input("name: ")
while True:
    try:
        age = int(input("Age: "))

        if age >= 18:
         print("you are eligible")
    except ValueError as r:
       print("can't help:", r)
    except Exception as f:
       print("Unexpected Error:", f)
    else:
     print("you are not eligible")
    gender = input("gender: ")
    courses = input("courses: ")
    user1 = {
        "name": name,
        "age": age,
        "gender": gender,
        "courses": [courses]
}
    print(f"{user1["name"]}\t{user1["age"]}\n{user1["gender"]}\t{user1["courses"]}")