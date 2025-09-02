from pathlib import Path

tasks = [] 

work_space = Path("workspace")
file = work_space / "note.csv"

def add_task(task):
    if task in tasks:
        tasks.append(task)
    print(task)

def remove_tasks(task):
    if task in tasks:
        tasks.remove(task)
        print(f"{tasks} as been appended")
    else:
        print(f"{task} already exist")

def view_task():
    if tasks:
        print(f"this are your available {tasks}")