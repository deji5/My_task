from track_2 import *


while True:
    print("\n My options")
    print("1: Add task")
    print("2: remove task")
    print("3: view task")
    print("4: exist")
    print("5: done")
    while True:
        options = input("enter option: ")
        
        for idx, row in enumerate(tasks, start=1):
            print(f"{idx:<10}{row['Task']:<35}{row['Date']:<15}")
        if options == "1":
            
            task = input("what task do you want to add: ").strip()
            
            if not task in tasks:
                with open(file, "r+", encoding = "utf-8") as p:
                    p.write(f"\n{task}")
                    tasks.append(task)
            print(tasks)
        else:
            print("wrong input")
        
        # break
    # while True:
        data = tasks
        if options == "2":
           for idx, row in enumerate(data, start=1):
                print(f"{idx:<10}{row['Task']:<35}{row['Date']:<15}")
           task = input('\n enter the row of what you want to delete')
           with open(file, "r+", encoding = "utf-8") as p:
                reader = csv.reader(p)
                data = list(reader)

           del data[task]
           with open(file, "w", encoding = "utf-8") as p:
               writer = csv.writer(p)
               writer.writerows(data)
        # break
            
        # task = input("enter the task you want to remove: ")
        # if task in tasks:
        #         tasks.remove(task) in file
        #         print(tasks)
    # while True:
        if options == "3":
            f = open(file, "r", encoding="utf-8")
            print(tasks)
            f.close()

        if options == "4":
            print("thank you,\nbye for now")
            break

        # inp = input("Done").title()
        # if inp == "5":
        #       break
        # print("good bye")