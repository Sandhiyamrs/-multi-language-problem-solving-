USERNAME = "admin"
PASSWORD = "1234"

attempts = 0
MAX_ATTEMPTS = 3

while attempts < MAX_ATTEMPTS:
    user = input("Username: ")
    pwd = input("Password: ")

    if user == USERNAME and pwd == PASSWORD:
        print("Login successful.")
        break
    else:
        attempts += 1
        print("Invalid credentials.")

if attempts == MAX_ATTEMPTS:
    print("Account locked due to too many failed attempts.")
