import csv
from pathlib import Path
import file_ops


work_space = Path("workspace")
# work_space.mkdir(exist_ok=True)
csv_file = work_space / "contacts.csv"

participant_dict = {}
while True:
    try:
        while True:
            try:
                name = input("enter your name: ").title()
                if not name.isalpha():
                    raise ValueError("enter correct input")
                else: 
                    participant_dict["name: "] = name
                break
            except ValueError as e:
                print("error",e)

        while True:
            try:
                age = input("enter your age: ")
                if not age.isdigit():
                    raise ValueError("invalid input")
                else: 
                    participant_dict["age"] = age
                break
            except ValueError as e:
                print("error",e)

        while True:
            try:    
                phone_num = input("Enter phone num: ")
                if phone_num.isdigit() and len(phone_num) == 12:
                    raise ValueError("invalid input")
                  
                else:
                    participant_dict["phone number"] = phone_num
                    break
            except ValueError as e:
                print("error",e)
        while True:
            try:
                track = input("enter track innvolvement:")
                if not track.isalpha():
                    raise ValueError("enter correct input")
                else: 
                    participant_dict["Track"] = track
                break
            except ValueError as e:
                print("error",e)
        file_ops.save_participant(csv_file, participant_dict)

    except ValueError as e:
        print("error:", e) 
        break

# participant_dict = {name, age, phone_num, track}
# try:
#     file_ops.save_participant()
# except:
#     print("try again")

# with open(csv_file, "a", newline="", encoding="utf-8") as p:
#     writer = csv.writer(p)

# writer.writerow(participant_dict)
# with open(csv_file, "a", newline="", encoding="utf-8") as p:
#     reader = csv.writer(p)
