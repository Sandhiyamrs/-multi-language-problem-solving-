balance = 0

while True:
    print("1. Deposit 2. Withdraw 3. Balance 4. Exit")
    choice = input("Choice: ")
    if choice == "1":
        amount = float(input("Deposit amount: "))
        balance += amount
    elif choice == "2":
        amount = float(input("Withdraw amount: "))
        if amount <= balance:
            balance -= amount
        else:
            print("Insufficient funds")
    elif choice == "3":
        print("Balance:", balance)
    elif choice == "4":
        break
    else:
        print("Invalid choice")
