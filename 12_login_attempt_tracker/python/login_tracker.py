MAX_ATTEMPTS = 3

attempts = 0

while attempts < MAX_ATTEMPTS:
    pwd = input("Enter password: ")
    if pwd == "admin123":
        print("Login successful")
        break
    else:
        attempts += 1
        print("Incorrect password")

if attempts == MAX_ATTEMPTS:
    print("Account locked")
