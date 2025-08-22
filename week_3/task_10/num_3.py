try:
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
except ValueError as r:
    print("can't help:", r)
except Exception as f:
    print("Unexpected Error:", f)