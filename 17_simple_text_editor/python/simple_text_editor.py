filename = input("Enter filename: ")
mode = input("Write(w) / Read(r): ").lower()

if mode == 'w':
    with open(filename, 'w') as f:
        print("Enter text (type 'END' on a new line to finish):")
        while True:
            line = input()
            if line == "END":
                break
            f.write(line + "\n")
elif mode == 'r':
    try:
        with open(filename) as f:
            print(f.read())
    except FileNotFoundError:
        print("File not found")
