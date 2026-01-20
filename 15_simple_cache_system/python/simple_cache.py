cache = {}

while True:
    print("\n1. Add to Cache")
    print("2. Get from Cache")
    print("3. View Cache")
    print("4. Exit")

    choice = input("Choice: ")

    if choice == "1":
        key = input("Key: ")
        value = input("Value: ")
        cache[key] = value
        print("Stored in cache.")

    elif choice == "2":
        key = input("Key: ")
        print("Value:", cache.get(key, "Key not found"))

    elif choice == "3":
        print("Cache Contents:")
        for k, v in cache.items():
            print(k, ":", v)

    elif choice == "4":
        break

    else:
        print("Invalid choice.")
