balance = 5000
pin = 1234
def check_balance():
    print("Current Balance: $" + str(balance))
def deposit():
    global balance
    amount = int(input("Enter Deposit Amount: $"))
    if amount >= 0:
        balance += amount
        print("Deposited: $" + str(amount))
        print("Current Balance: $" + str(balance))
    else:
        print("Invalid Deposit Amount")
def withdraw():
    global balance
    amount = int(input("Enter Withdraw Amount: $"))
    if amount > 0 and amount <= balance:
        balance -= amount
        print("Withdrawn: $" + str(amount))
        print("Current Balance: $" + str(balance))
def atm():
    user_pin = int(input("Enter Pin Number: "))
    if user_pin == pin:
        print("Login Successful")
        while True:
            print("\n1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")
            choice = int(input("Enter Choice: "))
            if choice == 1:
                check_balance()
            elif choice == 2:
                deposit()
            elif choice == 3:
                withdraw()
            elif choice == 4:
                exit()
            else:
                print("Invalid Choice")
    else:
        print("Invalid Pin")
atm()