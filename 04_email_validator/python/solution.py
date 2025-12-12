import re
email = input("Enter email: ")
pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,}$'
if re.match(pattern, email):
    print("Valid Email")
else:
    print("Invalid Email")

