import os
import shutil
import stat
from tkinter import Tk, filedialog

# Ekstensi file yang diizinkan
allowed_extensions = ['.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx',
                       '.pdf', '.txt', '.exe', '.rar', '.zip', '.7z', '.iso']

def handle_permission_error(func, path, exc_info):
    # Mengubah permission file menjadi writeable jika terjadi error
    os.chmod(path, stat.S_IWRITE)
    func(path)

def organize_files(directory):
    # Iterasi semua file dan folder di direktori
    for root, dirs, files in os.walk(directory, topdown=False):
        for name in files:
            file_path = os.path.join(root, name)
            file_ext = os.path.splitext(name)[1].lower()

            try:
                if file_ext in allowed_extensions:
                    # Buat folder berdasarkan ekstensi jika belum ada
                    target_folder = os.path.join(directory, file_ext.strip('.').upper())
                    os.makedirs(target_folder, exist_ok=True)

                    # Pindahkan file ke folder yang sesuai
                    shutil.move(file_path, os.path.join(target_folder, name))
                else:
                    # Hapus file yang tidak diizinkan
                    os.remove(file_path)
            except PermissionError:
                handle_permission_error(os.remove, file_path, None)

        for name in dirs:
            dir_path = os.path.join(root, name)
            try:
                # Hapus folder kosong
                if not os.listdir(dir_path):
                    os.rmdir(dir_path)
            except PermissionError:
                handle_permission_error(os.rmdir, dir_path, None)

# GUI untuk memilih folder
Tk().withdraw()  # Menyembunyikan jendela utama Tkinter
selected_directory = filedialog.askdirectory(title="Pilih Folder untuk Dieksekusi")

if selected_directory:
    organize_files(selected_directory)
    print(f"Proses selesai di folder: {selected_directory}")
else:
    print("Tidak ada folder yang dipilih.")
