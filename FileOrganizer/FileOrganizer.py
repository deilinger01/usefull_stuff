import os
import shutil

def organize_files(directory):
    if not os.path.exists(directory):
        print("Directory does not exist.")
        return

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            ext = filename.split('.')[-1].lower()
            folder_path = os.path.join(directory, ext)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            shutil.move(file_path, os.path.join(folder_path, filename))
    print("Files organized by extension.")

# Example usage
# organize_files("/path/to/directory")
