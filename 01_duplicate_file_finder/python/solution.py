import os
import hashlib
from collections import defaultdict

def get_file_hash(file_path, chunk_size=4096):
    hasher = hashlib.md5()
    with open(file_path, 'rb') as file:
        while chunk := file.read(chunk_size):
            hasher.update(chunk)
    return hasher.hexdigest()

def find_duplicates(directory):
    hashes = defaultdict(list)

    for root, _, files in os.walk(directory):
        for name in files:
            path = os.path.join(root, name)
            try:
                file_hash = get_file_hash(path)
                hashes[file_hash].append(path)
            except (PermissionError, OSError):
                pass

    return {h: paths for h, paths in hashes.items() if len(paths) > 1}

if __name__ == "__main__":
    folder = input("Enter directory path: ")
    duplicates = find_duplicates(folder)

    if not duplicates:
        print("No duplicate files found.")
    else:
        print("Duplicate files:")
        for files in duplicates.values():
            for file in files:
                print(file)
            print("-" * 40)
