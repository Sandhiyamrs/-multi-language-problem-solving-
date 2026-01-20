password = input("Enter password: ")

has_upper = any(c.isupper() for c in password)
has_lower = any(c.islower() for c in password)
has_digit = any(c.isdigit() for c in password)

score = sum([has_upper, has_lower, has_digit, len(password) >= 8])

if score <= 2:
    print("Weak Password")
elif score == 3:
    print("Medium Password")
else:
    print("Strong Password")
