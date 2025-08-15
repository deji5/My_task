name = input("enter your full name: ")
age = input("please your age")
gender = input("male/female")
courses = input("please name the courses u offer")
student_info ={
    'student name': name,
    'student age' : age,
    'stendent gender' : gender,
    'student courses' : courses
}
print(f"student name:\t{name}\nstudent age:\t{age}\nstudent gender:\t{gender}\nstudent courses:{[courses]}")