import re

url = input("Enter URL: ")
pattern = re.compile(r"^(https?://)?(www\.)?[a-zA-Z0-9-]+\.[a-z]{2,}(/.*)?$")
print("Valid URL" if pattern.match(url) else "Invalid URL")
