# Panduan GitHub Desktop untuk paket audit v18

## 1. Siapkan folder

Ekstrak ZIP paket ini. Buka folder `flood-report-audit-v18`. Di dalamnya harus terlihat `README.md`, `config`, `docs`, `notebooks`, `research_outputs`, dan folder lain. Jangan mengunggah ZIP saja karena reviewer perlu membaca struktur serta kode secara langsung.

## 2. Buat repositori melalui GitHub Desktop

Buka GitHub Desktop dan masuk ke akun Anda. Pilih **File > New repository** atau **Create a New Repository on your Hard Drive**. Isi Name dengan `flood-report-audit-v18`. Isi Description: `Exploratory flood-report prediction: code, aggregate evidence and audit provenance`. Pilih lokasi induk, misalnya Documents/GitHub. GitHub Desktop membuat subfolder dengan nama repositori.

Jangan centang Initialize with README karena paket sudah memuat README. Pilih Git ignore: None dan License: None pada tahap ini. Klik **Create repository**. Anda perlu menentukan lisensi kode yang memang Anda berhak terapkan sebelum rilis publik; lisensi dataset tidak otomatis melisensikan kode.

## 3. Salin ISI paket

Pada Desktop pilih **Repository > Show in Finder** di macOS atau **Show in Explorer** di Windows. Salin seluruh ISI folder hasil ekstraksi ke folder repositori ini. Jangan membuat susunan `flood-report-audit-v18/flood-report-audit-v18/README.md`. README harus berada tepat di akar repositori.

Pastikan `.gitignore` dan `.gitattributes` ikut tersalin. Pada macOS, Command+Shift+. menampilkan file tersembunyi. Pada Windows, gunakan View > Show > Hidden items. Jangan menyalin atau mengganti folder `.git` milik repositori.

## 4. Simpan commit pertama

Kembali ke tab **Changes**. Periksa bahwa notebook, konfigurasi dan 20 output masuk daftar. Ketik Summary: `Add v18 audit package and original research outputs`. Klik **Commit to main** atau nama branch yang muncul. Commit menyimpan perubahan secara lokal.

## 5. Publikasikan

Klik **Publish repository**. Pada tahap penyiapan, centang **Keep this code private** bila rekam komputasi belum lengkap atau naskah masih perlu pembatasan akses. Klik **Publish Repository**. Untuk rilis publik yang siap dibaca reviewer tanpa akun khusus, hilangkan centang tersebut saat publikasi atau ubah visibilitas setelah persiapan selesai. Pilih visibilitas sesuai proses review jurnal dan persetujuan penulis.

Pilih **Repository > View on GitHub**. Pastikan README tampil di halaman awal dan folder `research_outputs` memuat 10 PNG serta 10 CSV. Nama akun dan URL repositori harus berasal dari akun Anda; paket ini tidak mengarangnya.

## 6. Lengkapi hasil run asli

Ikuti `REPRODUCIBILITY.md` untuk mengekspor model, probabilitas, bukti training dan lingkungan dari Drive asli. Ekstrak ZIP tambahan dan periksa `export_status.json`. Jangan mengubah status missing menjadi complete tanpa berkas nyata. Arsipkan sumber CC BY 4.0 dengan atribusi atau cantumkan akses dan hash jika tidak menyertakannya. Perhatikan batas ukuran: GitHub memblokir berkas biasa yang melebihi 100 MiB. Untuk model besar gunakan aset release atau arsip data persisten; catat tautan dan checksum.

Salin berkas tambahan yang sudah diperiksa ke folder repositori sesuai jenisnya. Jangan menimpa keluaran lama dengan hasil run baru. Ubah dokumentasi kelengkapan dan buat commit baru, misalnya `Archive original fitted model and observation probabilities`. Klik **Push origin**. Commit saja belum mengirim pembaruan ke GitHub.

`provenance/file_manifest.json` memuat baseline paket awal. Setelah mengubah file baseline, regenerasi dengan `python scripts/update_manifest.py`, lalu jalankan `python scripts/verify_package.py`. Perintah tersebut juga bisa dijalankan dalam terminal VS Code atau Python lokal. Catat run baru terpisah apabila hash data/model berubah.

## 7. Buat release dan DOI melalui browser

Pembuatan arsip DOI membutuhkan browser selain Desktop. Hubungkan GitHub ke Zenodo, sinkronkan daftar repositori, lalu aktifkan repositori publik yang sesuai. Setelah integrasi aktif, buka repositori GitHub > **Releases > Draft a new release**. Buat tag `v18-audit-package-1`, pilih commit yang sudah Anda periksa, isi catatan tentang kelengkapan dan keterbatasan, lalu publikasikan release. Jangan menandai paket yang masih kurang sebagai reproduksi lengkap.

Tunggu Zenodo membuat rekaman. Periksa isi arsip, penulis, versi, lisensi, DOI dataset, serta DOI arsip kode. Salin DOI versi spesifik dan commit release yang benar ke pernyataan data/code availability. Mengunggah GitHub saja belum menghasilkan DOI. DOI sumber Mendeley berbeda dengan DOI arsip kode Anda. Jika hasil run asli baru lengkap kemudian, buat release baru dan gunakan DOI versi tersebut untuk naskah final.

## 8. Selesai bila

Reviewer dapat membuka repositori dan memperoleh versi arsip yang sama, memeriksa hash, membaca konfigurasi, dan menemukan berkas yang diperlukan. Penulis harus tetap menyatakan komponen yang belum tersedia. Kelengkapan repositori tidak menggantikan validasi ilmiah atau penilaian jurnal.

## Dokumentasi resmi

- https://docs.github.com/en/desktop/overview/creating-your-first-repository-using-github-desktop
- https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository
- https://docs.github.com/en/repositories/archiving-a-github-repository/referencing-and-citing-content
- https://help.zenodo.org/docs/github/enable-repository/
- https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github
