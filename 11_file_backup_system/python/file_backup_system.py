source = input("Enter source file: ")
backup = input("Enter backup file: ")

try:
    with open(source, "rb") as src:
        data = src.read()

    with open(backup, "wb") as dst:
        dst.write(data)

    print("Backup created successfully.")
except FileNotFoundError:
    print("Source file not found.")
