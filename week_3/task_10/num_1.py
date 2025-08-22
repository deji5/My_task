
while True:
        ussd_code = input("Enter ussd code (*145#)")
        if ussd_code == "*145#":
            print("welcome to paradise bank")
            break
        else:
            print("invalid input. Please input(*145#): ")
balance = 77000
while True:
        print("\nMenu: ")
        print("1. Check balance")
        print("2. Buy aitime")
        print("3. Tranfer")
        print("4. Buy data")
        print("5. Exit")
        try:    
            option = (input("enter choice: "))
            if option == "1":
                print(f"Your balance is:{balance}")
                break
            elif option == "2":
                amount = int(input("Enter airtime amount: "))
                if amount <= balance:
                    balance -= amount
                    print(f"Rechaage successful.\nNew balance: {balance}")
                    break
                else:
                    print(f"Insufficient funds.")
                    
            elif option == "3":
                tranfer = int(input("Enter amount: "))
                if tranfer <= balance:
                    balance -= tranfer
                    print(f"Transfer successful.\nNew balance: {balance}")
                    break
                else:
                    print(f"Insufficient funds.")
            elif option == "4":
                amount = int(input("Enter data amount: "))
                if amount <= balance:
                    balance -= amount
                    print(f"Rechaage successful.\nNew balance: {balance}")
                    break
                else:
                    print(f"Insufficient funds.")
            elif option == "5":
                    print(f"thank you for banking with paradise bank.")
                    break
            else:
                    print(f"Try Again.")                      
        except ValueError as e:
            print(f"invalid {e}")