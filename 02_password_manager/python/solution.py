import hashlib

password_store = {}

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def add_password(service, password):
    if service in password_store:
        print("Service already exists.")
        return
    password_store[service] = hash_password(password)
    print("Password stored successfully.")

def retrieve_password(service):
    if service not in password_store:
        print("Service not found.")
        return
    print(f"Stored hash for {service}: {password_store[service]}")

def menu():
    while True:
        print("\n1. Add Password")
        print("2. Retrieve Password")
        print("3. Exit")
        choice = input("Choose option: ")

        if choice == "1":
            service = input("Service name: ")
            password = input("Password: ")
            add_password(service, password)
        elif choice == "2":
            service = input("Service name: ")
            retrieve_password(service)
        elif choice == "3":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    menu()
