# Organize Files Script

## Deskripsi
Script Python ini digunakan untuk mengelola file dalam sebuah folder dengan cara:
- Menghapus semua file dan folder kecuali file dengan ekstensi tertentu.
- Mengelompokkan file yang diizinkan ke dalam folder berdasarkan ekstensinya.
- Menangani masalah izin akses file (permission error) secara otomatis.

## Ekstensi yang Diizinkan
- Microsoft Word: `.doc`, `.docx`
- Microsoft Excel: `.xls`, `.xlsx`
- Microsoft PowerPoint: `.ppt`, `.pptx`
- Dokumen: `.pdf`, `.txt`
- Aplikasi & Arsip: `.exe`, `.rar`, `.zip`, `.7z`, `.iso`

## Cara Menggunakan
1. **Persyaratan:**
   - Pastikan Python sudah terinstal di komputer Anda.

2. **Jalankan Script:**
   - Simpan script sebagai `organize_files.py`.
   - Buka terminal atau command prompt.
   - Jalankan perintah berikut:
     ```bash
     python organize_files.py
     ```

3. **Pilih Folder:**
   - Jendela pemilihan folder akan muncul.
   - Pilih folder yang ingin dikelola dan klik **OK**.

4. **Proses:**
   - Script akan memproses folder:
     - Memindahkan file dengan ekstensi yang diizinkan ke folder berdasarkan ekstensinya.
     - Menghapus file yang tidak diizinkan.
     - Menghapus folder kosong.

5. **Hasil:**
   - Folder baru akan dibuat berdasarkan ekstensi file (misalnya: `PDF`, `DOCX`, `ZIP`).

## Fitur Tambahan
- **Penanganan Izin (Permission Error):**
  - Script secara otomatis akan mengubah izin file untuk mengatasi masalah akses yang terbatas.

## Catatan Penting
- **Backup Data:** Sebaiknya buat cadangan data sebelum menjalankan script ini, karena file yang tidak diizinkan akan dihapus permanen.
- **Hak Akses:** Untuk folder dengan izin terbatas, jalankan terminal sebagai **Administrator**.

## Lisensi
Script ini bebas digunakan dan dimodifikasi sesuai kebutuhan.

