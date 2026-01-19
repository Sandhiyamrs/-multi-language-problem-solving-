import re

EMAIL_REGEX = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

def is_valid_email(email: str) -> bool:
    return re.match(EMAIL_REGEX, email) is not None

def main():
    email = input("Enter email address: ").strip()
    if is_valid_email(email):
        print("Valid email address.")
    else:
        print("Invalid email address.")

if __name__ == "__main__":
    main()

