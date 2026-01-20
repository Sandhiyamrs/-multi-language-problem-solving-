filename = input("Enter log file name: ")

error = warning = info = 0

try:
    with open(filename, "r") as file:
        for line in file:
            if "ERROR" in line:
                error += 1
            elif "WARNING" in line:
                warning += 1
            elif "INFO" in line:
                info += 1

    print("\nLog Summary:")
    print("ERROR:", error)
    print("WARNING:", warning)
    print("INFO:", info)

except FileNotFoundError:
    print("Log file not found.")
