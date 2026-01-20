key = 123

input_file = input("Input file: ")
output_file = input("Output file: ")

with open(input_file, "rb") as f:
    data = f.read()

encrypted = bytes([b ^ key for b in data])

with open(output_file, "wb") as f:
    f.write(encrypted)

print("File encrypted successfully.")
