balance = 0.0

while True:
    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Choice: ")

    if choice == "1":
        print("Balance:", balance)

    elif choice == "2":
        amount = float(input("Enter amount: "))
        balance += amount
        print("Amount deposited.")

    elif choice == "3":
        amount = float(input("Enter amount: "))
        if amount <= balance:
            balance -= amount
            print("Amount withdrawn.")
        else:
            print("Insufficient balance.")

    elif choice == "4":
        break

    else:
        print("Invalid choice.")
