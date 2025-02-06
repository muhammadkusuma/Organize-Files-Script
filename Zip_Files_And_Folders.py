import os
import zipfile
import tkinter as tk
from tkinter import filedialog

def zip_files_in_folder(folder_path):
    """Membuat zip dari semua file dalam folder."""
    zip_name = f"{folder_path}.zip"
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, folder_path)
                zipf.write(file_path, arcname)
    print(f"Files in {folder_path} have been zipped into {zip_name}")

def zip_folders(base_path):
    """Meng-zip setiap folder dalam direktori, lalu meng-zip folder-folder tersebut."""
    folder_zips = []
    for item in os.listdir(base_path):
        item_path = os.path.join(base_path, item)
        if os.path.isdir(item_path):
            zip_files_in_folder(item_path)
            folder_zips.append(f"{item_path}.zip")
    
    # Zip semua folder yang telah di-zip
    master_zip = os.path.join(base_path, "all_folders.zip")
    with zipfile.ZipFile(master_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for folder_zip in folder_zips:
            zipf.write(folder_zip, os.path.basename(folder_zip))
    print(f"All folders have been zipped into {master_zip}")

def select_folder():
    root = tk.Tk()
    root.withdraw()
    folder_selected = filedialog.askdirectory()
    return folder_selected

if __name__ == "__main__":
    base_directory = select_folder()
    if base_directory:
        zip_folders(base_directory)
