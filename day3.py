 

usersDetail = []

while True:
    print("\nWhat would you like to do today in our bank?")
    print("*" * 40)
    print("      WELCOME TO YOUR BANKING SYSTEM")
    print("*" * 40)
    print("1. create an account")
    print("2. login your account")
    print("3. make a deposit")
    print("4. make a withdrawal")
    print("5. check balance")
    print("6. transaction history")
    print("7. logout")
    print("8. exit")
    print("-" * 40)

    choice = input("Enter your choice (1-8): ")

# creating an account
    if choice == "1":
        username = input("Enter the user's name: ")
        password = input("Enter the user's password: ")
        pin= input("Enter the user's pin: ")
        balance = 0.0
        usersDetail.append((username, password, pin, login, balance))
        print(f"User added: {username} with initial balance of {balance}")

        # login to the account
    elif choice == "2":
        username = input("Enter your username: ")
        entered_password = input("Enter your password: ")
        user_found = False
        if usersDetail:
            print("\nUsers:")
            for name, password, pin, login, balance in usersDetail:
                if name == username and password == entered_password:
                    user_found = True
                    print(f"Name: {name}, Balance: {balance}")
        else:
            print("No users to display.")
        if not user_found:
            print("Invalid username or password.")

     # make a deposit 
    elif choice == "3":
        username = input("Enter your username: ")
        deposit_amount = float(input("Enter the amount to deposit: "))
        user_found = False
        for i, (name, password, pin, login, balance) in enumerate(usersDetail):
            if name == username:
                user_found = True
                usersDetail[i] = (name, password, pin, login, balance + deposit_amount)
                print(f"Deposit successful. New balance: {usersDetail[i][4]}")
                break
        if not user_found:
            print("User not found.")
     # make a withdrawal
    elif choice == "4": 
        username = input("Enter your username: ")
        withdrawal_amount = float(input("Enter the amount to withdraw: "))
        user_found = False
        for i, (name, password, pin, login, balance) in enumerate(usersDetail):
            if name == username:
                user_found = True
                if withdrawal_amount <= balance:
                    usersDetail[i] = (name, password, pin, login, balance - withdrawal_amount)
                    print(f"Withdrawal successful. New balance: {usersDetail[i][4]}")
                else:
                    print("Insufficient funds.")
                break
        if not user_found:
            print("User not found.")
    elif choice == "5":
        username = input("Enter your username: ")
        user_found = False
        for name, password, pin, login, balance in usersDetail:
            if name == username:
                user_found = True
                print(f"Current balance for {name}: {balance}")
                break
        if not user_found:
            print("User not found.")  
     
     # check transaction history
    elif choice == "6":
        username = input("Enter your username: ")
        user_found = False
        for name, password, pin, login, balance in usersDetail:
            if name == username:
                user_found = True
                print(f"Transaction history for {name}:")
                print(f"Balance: {balance}")
                break
        if not user_found:
            print("User not found.")  
            
    # logout
    elif choice == "7":
        print("Logging out...")
        break
    # exit
    elif choice == "8":
        print("Thank you for using our banking system.")
        break
    else:
        print("Invalid choice. Please enter a number between 1-8.")