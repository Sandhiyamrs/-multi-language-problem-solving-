import os
import shutil

def backup_files(source, backup):
    if not os.path.exists(source):
        print("Source folder not found")
        return

    os.makedirs(backup, exist_ok=True)

    for file in os.listdir(source):
        src_file = os.path.join(source, file)
        dest_file = os.path.join(backup, file)

        if os.path.isfile(src_file):
            shutil.copy2(src_file, dest_file)
            print(f"Backed up: {file}")

if __name__ == "__main__":
    backup_files("source", "backup")
