poll = {
    "Option A": 0,
    "Option B": 0,
    "Option C": 0
}

while True:
    print("\n1. Vote")
    print("2. View Results")
    print("3. Exit")

    choice = input("Choice: ")

    if choice == "1":
        print("\nOptions:")
        for i, option in enumerate(poll.keys(), start=1):
            print(i, option)

        vote = int(input("Select option number: "))
        options = list(poll.keys())

        if 1 <= vote <= len(options):
            poll[options[vote - 1]] += 1
            print("Vote recorded.")
        else:
            print("Invalid option.")

    elif choice == "2":
        print("\nResults:")
        for option, count in poll.items():
            print(option, ":", count)

    elif choice == "3":
        break

    else:
        print("Invalid choice.")
