tasks = []

def show_tasks():
    if not tasks:
        print("No tasks available.")
        return
    for i, task in enumerate(tasks, start=1):
        status = "✓" if task["done"] else " "
        print(f"{i}. [{status}] {task['title']}")

def add_task():
    title = input("Task title: ").strip()
    if title:
        tasks.append({"title": title, "done": False})
        print("Task added.")
    else:
        print("Task title cannot be empty.")

def mark_complete():
    show_tasks()
    try:
        index = int(input("Task number to mark complete: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["done"] = True
            print("Task marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input.")

def delete_task():
    show_tasks()
    try:
        index = int(input("Task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            tasks.pop(index)
            print("Task deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input.")

def menu():
    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            mark_complete()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    menu()
