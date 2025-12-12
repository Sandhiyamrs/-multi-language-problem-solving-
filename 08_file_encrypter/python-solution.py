def encrypt_decrypt(file_path, key):
    with open(file_path, 'rb') as f:
        data = f.read()
    result = bytes([b ^ key for b in data])
    with open(file_path + ".enc", 'wb') as f:
        f.write(result)
    print("File processed!")

file = input("File path: ")
k = int(input("Enter numeric key: "))
encrypt_decrypt(file, k)
