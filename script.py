import os
import shutil

images = ['.jpg', '.jpeg', '.png']
documents = ['.pdf', '.doc', '.docx', '.txt']


directory_path = input("Enter the path of your new folder: ")

try:
    with os.scandir(directory_path) as entries:
        for entry in entries:
            if entry.is_file() :
                ext = os.path.splitext(entry.name)
                if ext[1] in documents:
                    documents_folder = "Documents"
                    documents_path = os.path.join(directory_path, documents_folder)
                    os.makedirs(documents_path, exist_ok=True)
                    print(f"{entry.name} -> {documents_path}")
                    shutil.move(entry, documents_path)
                elif ext[1] in images:
                    images_folder = "Images"
                    images_path = os.path.join(directory_path, images_folder)
                    os.makedirs(images_path, exist_ok=True)
                    print(f"{entry.name} -> {images_path}")
                    shutil.move(entry, images_path)
except FileNotFoundError:
    print(f"Error: Directory '{directory_path}' doesn't exist.")
except OSError as e:
    print(f"Error creating Directory: '{e}'")






