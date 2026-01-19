expenses = []

def add_expense(amount, category):
    expenses.append((amount, category))
    print("Expense added.")

def show_total():
    total = sum(amount for amount, _ in expenses)
    print(f"Total expenses: {total:.2f}")

def show_by_category():
    category_totals = {}
    for amount, category in expenses:
        category_totals[category] = category_totals.get(category, 0) + amount

    for category, total in category_totals.items():
        print(f"{category}: {total:.2f}")

def menu():
    while True:
        print("\n1. Add Expense")
        print("2. View Total")
        print("3. View by Category")
        print("4. Exit")
        choice = input("Choose option: ")

        if choice == "1":
            try:
                amount = float(input("Amount: "))
                category = input("Category: ")
                add_expense(amount, category)
            except ValueError:
                print("Invalid amount.")
        elif choice == "2":
            show_total()
        elif choice == "3":
            show_by_category()
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    menu()
