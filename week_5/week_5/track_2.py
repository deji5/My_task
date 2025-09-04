import csv
from pathlib import Path

tasks = [] 

work_space = Path("workspace")
work_space.mkdir(exist_ok = True)
file = work_space / "note.csv"

def add_task(task):
    if task in tasks:
        tasks.append(task)
    print(task)

# def remove_tasks(task):
#     if task in tasks:
#         tasks.remove(task)
#         print(f"{tasks} as been appended")
#     else:
#         print(f"{task} already exist")


def DEL():
    try:
        for line in file:
            task = [value.replace(tasks, "")for value in line]

    except:
        print("NOPE")
def view_task():
    if tasks:
        print(f"this are your available {tasks}")