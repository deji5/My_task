school_name = input("enter name")
tuition_fee = float(input("enter tution fee"))
hostel_fee = float(input("enter hostel fee"))
feeding_fee = float(input("enter feeding fee"))
total = tuition_fee + hostel_fee + feeding_fee
print(f"school name\t{school_name}\namount for tution\t{tuition_fee}\nhostel fee\t{hostel_fee}\nfeeding fee\t{feeding_fee}\ntotal\t{total:.2f}")