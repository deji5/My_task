from track_2 import *


while True:
    print("\n My options")
    print("1: Add task")
    print("2: remove task")
    print("3: view task")
    print("4: exist")
    while True:
        options = input("enter option: ")
        f = open(file, "a", encoding="utf-8")
        
        if options == "1":
            task = input("what task do you want to add: ")
            if not task in tasks:
                f.write(f"\n{task}")
                tasks.append(task)
            
        
            print(tasks)
        else:
            None, None
        f.close()
        if options == "2":
            f = open(file, "r", encoding="utf-8")
            
            task = input("enter the task you want to remove: ")
            if task in tasks:
                if "r" in tasks.remove(task) in f:
                    print(tasks)
            f.close()   

        if options == "3":
            f = open(file, "r", encoding="utf-8")
            print(tasks)
            f.close()

        if options == "4":
            print("thank you,\nbye for now")
            break