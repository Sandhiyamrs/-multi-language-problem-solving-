import re

pwd = input("Enter password: ")

strength = "Weak"
if (len(pwd) >= 8 and re.search(r"[A-Z]", pwd) and
    re.search(r"[a-z]", pwd) and re.search(r"[0-9]", pwd) and
    re.search(r"[@#$%^&+=]", pwd)):
    strength = "Strong"
elif len(pwd) >= 6:
    strength = "Medium"

print("Password strength:", strength)
