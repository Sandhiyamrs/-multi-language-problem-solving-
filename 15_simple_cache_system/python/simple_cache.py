cache = {}

while True:
    key = input("Key (exit to quit): ")
    if key == "exit":
        break
    value = input("Value: ")
    cache[key] = value
    print("Cached:", cache)
