import csv
from pathlib import Path

work_space = Path("workspace")
work_space.mkdir(exist_ok=True)
csv_file = work_space / "contacts.csv"

# participants = {}

def save_participant(path, participant_dict):

    fieldnames = participant_dict.keys()
    with open(path, "a", encoding="utf-8", newline = "") as p:
        participants = {"Name", "Age", "Course", "Grade"}
        fileexist = csv_file.exists() 
        saving = csv.DictWriter(p, fieldnames = fieldnames)
        if not fileexist :
            saving.writeheader(participants)
        saving.writerow(participant_dict)

print("Participant data's saved!")

def load_participants(Path):
    with open(csv_file, "r", encoding="utf-8") as p:
        reader = csv.reader(p)

        for row_numer in enumerate(reader):
            if row_numer == 0:
                print(f"Headers:")


