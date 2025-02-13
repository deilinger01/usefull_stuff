import os
import hashlib

def find_duplicate_files(directory):
    if not os.path.exists(directory):
        print("Directory does not exist.")
        return

    hash_map = {}
    duplicates = []

    for root, _, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            with open(file_path, 'rb') as f:
                file_hash = hashlib.md5(f.read()).hexdigest()
                if file_hash in hash_map:
                    duplicates.append(file_path)
                else:
                    hash_map[file_hash] = file_path

    if duplicates:
        print("Duplicate files found:")
        for dup in duplicates:
            print(dup)
    else:
        print("No duplicate files found.")

# Example usage
# find_duplicate_files("/path/to/directory")
