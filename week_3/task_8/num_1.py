num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(f"{num1} == {num2} : {num1 == num2}") 
# first and second number are equal to each it will return true but if not return false
# 10 == 10 # True
# 5 == 10  # False

print(f"{num1} != {num2} : {num1 != num2}")
# != means they shouldnt be equal and if they are equal write false
# 1 != 2 True
# 2 != 2 False

print(f"{num1} > {num2} : {num1 > num2}")
# > it simply mean is the first number greater than the second munber if it is  write true and if it is not write false write 
# 8 > 9 false due to the fact that 8 is smaller than 9
# 9 > 3 true due to the fact that 9 is bigger than 3

print(f"{num1} < {num2} : {num1 < num2}")
# < it simply mean is the first number lesser than the second munber if it is  write true and if it is not write false write 
# 8 < 9 true due to the fact that 8 is smaller than 9
# 9 < 3 false due to the fact that 9 is bigger than 3


# the 3 cases where they can be usedor applied:
# 1. it can be used for monitring grades
# 2. it is used to gage prices
# 3. it is used to compare height

math_grade = int(input("Enter math grade"))
previous_grade = int(input("Enter previous grade"))
print(f"{math_grade} == {previous_grade} : {math_grade == previous_grade}")