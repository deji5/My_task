# #  Collecting applicant detail
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# score = int(input("Enter your test score: "))
# # confirming if the apllicants are of age and reached the pass mark
# # if the applicant is of age and reached the pass mark it will return as true
# eligibility = (age < 18) and (score > 70)
# print(f"Candidate: {name}\nAge: {age}\nScore: {score}\nEligible: {eligibility}")



name = input("enter your name").title()
nationality = input("enter your country")
enrollment = input("are presently enrolloed in any university as a full time")
other_scholarship = input("are currently recieving scholarship from any oil and gas industry")
academy_qualification = input("how many distinction do u have")
eligibility = (nationality == "Nigeria"or "nigeria" or "NIGERIA") and (enrollment == "full time" or  "Full time" or "FULL TIME") and (other_scholarship == "No" or "no" or "NO") and (academy_qualification >= 5)
print(f"Citizen name: {name}\nNationality: {nationality}\nEnrollment: {enrollment}\nOther scholarship: {other_scholarship}\nAcademic Qualification: {academy_qualification}")
print("eligibility:", eligibility)