count = 0
with open("app.log") as file:
    for line in file:
        if "ERROR" in line:
            count += 1
print("Error count:", count)
