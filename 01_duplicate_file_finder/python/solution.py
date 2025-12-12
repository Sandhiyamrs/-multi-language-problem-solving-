import os
import hashlib

def md5_hash(path):
    hasher = hashlib.md5()
    with open(path, 'rb') as f:
        hasher.update(f.read())
    return hasher.hexdigest()

def find_duplicates(folder_path):
    seen = {}
    duplicates = []

    for root, _, files in os.walk(folder_path):
        for file in files:
            full_path = os.path.join(root, file)
            try:
                file_hash = md5_hash(full_path)
            except Exception:
                continue
            if file_hash in seen:
                duplicates.append((full_path, seen[file_hash], os.path.getsize(full_path)))
            else:
                seen[file_hash] = full_path

    return duplicates

folder = input("Enter folder path: ")
dups = find_duplicates(folder)

if dups:
    total_size = sum([s for _,_,s in dups])
    print("\nDuplicate files found:")
    for f1, f2, _ in dups:
        print(f"{f1} == {f2}")
    print(f"Total duplicates: {len(dups)}")
    print(f"Total space wasted: {total_size/1024:.2f} KB")
else:
    print("No duplicates found.")

