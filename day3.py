 

usersDetail = []

while True:
    print("\nWhat would you like to do today in our bank?")
    print("1. create an account")
    print("2. login your account")
    print("3. make a deposit")
    print("4. make a withdrawal")
    print("5. check balance")
    print("-" * 40)

    choice = input("Enter your choice (1-5): ")

# creating an account
    if choice == "1":
        username = input("Enter the user's name: ")
        password = input("Enter the user's password: ")
        pin= input("Enter the user's pin: ")
        login = input("Enter the user's login: ")
        balance = 0.0
        usersDetail.append((username, password, pin, login, balance))
        print(f"User added: {username}")

        # login to the account
    elif choice == "2":
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        user_found = False
        if usersDetail:
            print("\nUsers:")
            for name, password, pin, login, balance in usersDetail:
                if name == username and password == password:
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
        
    else:
        print("Invalid choice. Please enter a number between 1-5.")