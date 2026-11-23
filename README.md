# Praktikum Flask: Parsing Parameter Form Pakai Method POST

Repositori ini berisi catatan dan kode praktikum web sederhana menggunakan **Flask** untuk menerima dan mengolah data dari formulir HTML lewat metode **`POST`**, lengkap dengan tampilan *card* bernuansa ungu lavender/lilac[cite: 3].

---

## Tentang Project Ini
Di praktikum ini, aku bikin halaman form sederhana yang ngirim data pakai `method="POST"` ke server Flask. Alurnya simpel:
- Pas halaman dibuka (`GET`), *browser* nampilin form dengan label **Nama Lengkap:**, kotak input (*text field*) ber-*placeholder* `"Masukkan nama di sini..."`, dan tombol **Kirim**[cite: 3].
- Pas tombol **Kirim** diklik, data dikirim lewat `POST` dan ditangkap di `app.py` pakai `request.form`.
- Inputnya dibersihin dulu pakai `.strip()` biar spasi kepencet di awal/akhir nggak ikut kehitung, terus dicek kosong atau nggak sebelum ditampilin hasilnya ke layar.

---

## Susunan Folder & File
```text
FirstFlask_138/
├── app.py              # Route Flask, handle GET & POST, plus ambil data form
├── README.md           # Catatan dokumentasi praktikum
├── static/
│   └── styles.css      # Styling tema ungu lavender/lilac, posisi tengah layar, & efek fokus input[cite: 3]
└── templates/
    └── index.html      # Tampilan form (label, input text, tombol submit) & blok hasil/error[cite: 3]
