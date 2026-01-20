text = []

while True:
    print("\n1. Add Text")
    print("2. View Text")
    print("3. Clear Text")
    print("4. Exit")

    choice = input("Choice: ")

    if choice == "1":
        line = input("Enter text: ")
        text.append(line)

    elif choice == "2":
        print("\nCurrent Text:")
        for line in text:
            print(line)

    elif choice == "3":
        text.clear()
        print("Text cleared.")

    elif choice == "4":
        break

    else:
        print("Invalid choice.")
