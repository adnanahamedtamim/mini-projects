print("\n//***********Banking System***********//")

account_number = 0
database = {}

while True:
    print("\n\nPlease, Enter the index of the operations to be done")
    print("\n\n1.Create Account")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Balance Check")
    print("5.Delete Account")
    print("6.Account Details")
    print("7.Quit")
    
    index = int(input("\n\nindex :: "))

    if index == 1: 
        name = input("Enter your name : ")
        email = input("Enter your email : ")
        password = input("Enter a password : ")
        database[account_number] = {
            "name" : name,
            "email": email,
            "balance" : 0,
            "password": password
        }
        print("\nAccount creation done")
        print("Your Account Number is " + str(account_number))
        account_number += 1

    elif index == 2:
        accnt = int(input("Enter Account Number : "))
        amnt = int(input("Enter Amount : "))
        
        if accnt not in database:   #database.get(accnt)==None can be used also ``
            print("\n Invalid account number")
            continue
        
        password = input("Enter Password : ")
        if database[accnt]["password"] != password:
            print("\nIncorrect Password")
            continue

        database[accnt]["balance"] += amnt 
        print("\nMoney Deposited Successfully")

    elif index == 3: 
        accnt = int(input("Enter Account Number : "))
        amnt = int(input("Enter Amount : "))

        if accnt not in database:
            print("\n Invalid account number")
            continue

        password = input("Enter Password : ")
        if database[accnt]["password"] != password:
            print("\nIncorrect Password")
            continue

        if database[accnt]["balance"] < amnt:
            print("\nInsufficient balance")
            continue

        database[accnt]["balance"] -= amnt
        print("\nMoney Withdrawn Successfully")

    elif index == 4: 
        accnt = int(input("Enter Account Number : "))
        
        if accnt not in database:
            print("\n Invalid account number")
            continue

        password = input("Enter Password : ")
        if database[accnt]["password"] != password:
            print("\nIncorrect Password")
            continue

        print("\nYour current balance is : " + str(database[accnt]["balance"]))

    elif index == 5: 
        accnt = int(input("Enter Account Number : "))
        
        if accnt not in database:
            print("\n Invalid account number")
            continue

        password = input("Enter Password : ")
        if database[accnt]["password"] != password:
            print("\nIncorrect Password")
            continue

        del database[accnt]
        print("\nAccount Deleted Successfully")

    elif index == 6:
        accnt = int(input("Enter Account Number : "))
        
        if accnt not in database:
            print("\n Invalid account number")
            continue

        password = input("Enter Password : ")
        if database[accnt]["password"] != password:
            print("\nIncorrect Password")
            continue

        print("\nName : " + str(database[accnt]["name"]))
        print("email : " + str(database[accnt]["email"]))
        print("Balance : " + str(database[accnt]["balance"]))
    
    elif index == 7:
        print("\nSee you again")
        break

    else: 
        print("\nInvalid Index")
