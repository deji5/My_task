# name = input("enter your name").title()
# nationality = input("enter your country").title()
# enrollment = input("are presently enrolloed in any university as a full time").title()
# other_scholarship = input("are currently recieving scholarship from any oil and gas industry").title()
# academy_qualification = input("how many distinction do u have")
# eligibility = (nationality == "Nigeria") and (enrollment == "Yes") and (other_scholarship == "No") and (academy_qualification == "5")
# print(f"Citizen name: {name}\nNationality: {nationality}\nEnrollment: {enrollment}\nOther scholarship: {other_scholarship}\nAcademic Qualification: {academy_qualification}")
# print("eligibility:", eligibility)

while True:
    name = input("Enter your full name: ").title()
    citizenhip =input("enter your nationality: ").title()
    enrollment = input("Are you a fulltime student: ").title()
    other_scholarship = input("are currently recieving scholarship from any oil and gas industry").title()
    academy_qualification = input("how many distinction do u have")
    eligibility = (citizenhip == "Nigerian") and (enrollment == "Yes") and (other_scholarship == "No") and ( academy_qualification >= "5") 
    print("Eligibilty", eligibility)
    end = input("do you want to end yes or no").lower()
    if end == 'yes':
        print("end of registration")
        break
    else:
        end == 'no'
        print("Okay continue")
        continue 
