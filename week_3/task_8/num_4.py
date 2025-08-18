student = {}
Name = input("Enter name")
age = int(input("enter age"))
score = [70, 85, 90]
student = {
    "name": Name,
    "age": age,
    "score": score

}
passed = (score >= 50)
teenager = (age > 13) and (age < 19)
print(f"Name: {Name}\nAge: {age}\nScores: {score}\nPassed: {passed}\nTeenager: {teenager}")