students = []

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Show Average")
    print("4. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        name = input("Student name: ")
        grade = float(input("Grade: "))
        students.append((name, grade))
        print("Student added.")

    elif choice == "2":
        if not students:
            print("No students available.")
        for name, grade in students:
            print(f"{name}: {grade}")

    elif choice == "3":
        if students:
            avg = sum(g for _, g in students) / len(students)
            print("Class Average:", avg)
        else:
            print("No grades to calculate.")

    elif choice == "4":
        break

    else:
        print("Invalid choice.")
