import hashlib
import os

def sha256sum(filename):
    """Menghitung SHA-256 checksum dari file."""
    sha256 = hashlib.sha256()
    with open(filename, 'rb') as f:
        while chunk := f.read(8192):
            sha256.update(chunk)
    return sha256.hexdigest()

def save_checksum(zip_file):
    """Menyimpan checksum SHA-256 ke file dengan nama sesuai zip file."""
    checksum = sha256sum(zip_file)
    checksum_filename = f"{zip_file}.txt"
    
    with open(checksum_filename, 'w') as f:
        f.write(f"SHA-256: {checksum}\n")
    
    print(f"Checksum disimpan di: {checksum_filename}")

def process_folder(folder_path):
    """Memproses semua file ZIP dalam folder."""
    if not os.path.exists(folder_path):
        print("Folder tidak ditemukan.")
        return
    
    for file in os.listdir(folder_path):
        if file.endswith('.zip'):
            zip_path = os.path.join(folder_path, file)
            save_checksum(zip_path)

if __name__ == "__main__":
    folder_path = input("Masukkan path folder yang berisi file ZIP: ")
    process_folder(folder_path)
