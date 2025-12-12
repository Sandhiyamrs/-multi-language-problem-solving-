import random
import string

def generate_password(length=12):
    if length < 8:
        print("Password too short! Minimum 8 characters.")
        return None
    all_chars = string.ascii_letters + string.digits + string.punctuation
    while True:
        password = ''.join(random.choice(all_chars) for _ in range(length))
        if (any(c.islower() for c in password) and
            any(c.isupper() for c in password) and
            any(c.isdigit() for c in password) and
            any(c in string.punctuation for c in password)):
            return password

num = int(input("How many passwords to generate? "))
length = int(input("Password length: "))
passwords = [generate_password(length) for _ in range(num)]
for idx, pwd in enumerate(passwords,1):
    print(f"{idx}: {pwd}")

save = input("Save passwords to file? (y/n): ").lower()
if save == 'y':
    with open("passwords.txt","w") as f:
        for pwd in passwords:
            f.write(pwd+"\n")
    print("Saved to passwords.txt")

