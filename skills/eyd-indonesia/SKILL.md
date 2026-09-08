---
name: eyd-indonesia
description: Use when editing, proofreading, or correcting Indonesian text spelling, punctuation, and grammar according to official EYD V (Ejaan Bahasa Indonesia yang Disempurnakan Edisi V). Use for capital letters, italics, bold, affixes, prepositions, particles, abbreviations, numbers, coordinating conjunctions ("dan" vs "serta"), Oxford comma, punctuation, and loanwords.
tags: [indonesian, eyd, eyd-v, proofreading, grammar, ejaan]
---

# EYD Indonesia (Edisi V)

Skill ini menggunakan **Pendekatan Hibrida**: menggabungkan ringkasan kaidah kritis internal (*cheat-sheet*) untuk eksekusi cepat, serta peta indeks 35+ URL resmi EYD V untuk verifikasi kasus batas (*edge cases*) secara langsung.

## 1. Pendekatan Hibrida & Rujukan

* **Rujukan Cepat Internal**: Sebelum menyunting atau melakukan pemanggilan web, baca [Ringkasan Kaidah Kritis](references/ringkasan-kaidah.md) untuk memeriksa aturan rawan salah yang paling sering ditemukan.
* **Kaidah Konjungsi "Dan" vs "Serta"**: Pelajari rujukan detail di [Panduan Penggunaan Kata "Dan" dan "Serta"](references/konjungsi-dan-serta.md) untuk memastikan ketepatan semantis, penempatan tanda koma (2 unsur vs >2 unsur/Oxford comma), perincian bertingkat, serta eliminasi pleonasme "dan serta".
* **Verifikasi Online Presisi**: Jika aturan diragukan, memerlukan contoh spesifik, atau terdapat kata serapan asing yang berpotensi diperdebatkan, gunakan `webfetch` langsung ke URL spesifik dari [Peta Indeks Sumber Resmi](references/sumber-resmi.md).

## 2. Alur Kerja Penyuntingan

1. **Analisis Konteks & Proteksi Teks**:
   - Tentukan ragam teks (akademik, formal, populer, sastra).
   - DILARANG mengubah nama diri, istilah merek, kutipan langsung, kode program, URL, rumus, atau slogan tanpa instruksi spesifik.
2. **Pemeriksaan Berurutan**:
   - **Penggunaan Huruf**: Huruf kapital, miring, dan tebal.
   - **Penulisan Kata**: Kata berimbuhan, kata depan (`di`/`ke`), bentuk terikat (`pasca-`, `sub-`, `maha-`), partikel (`pun`), singkatan/akronim, serta angka & bilangan.
   - **Penggunaan Tanda Baca & Konjungsi Koordinatif**:
     - Titik, titik dua, tanda hubung, tanda pisah (`—`), elipsis, dan tanda petik.
     - Konjungsi Pertentangan: koma sebelum *tetapi*, *melainkan*, *sedangkan*.
     - Konjungsi Koordinatif (*Dan* vs *Serta*):
       - **2 Unsur**: Tanpa tanda koma (*"A dan B"*; *"X serta Y"*).
       - **> 2 Unsur**: Wajib tanda koma sebelum konjungsi terakhir / Oxford comma (*"A, B, dan C"*; *"X, Y, serta Z"*).
       - **Distingsi Makna**: Gunakan *dan* untuk relasi kesetaraan murni berbobot sama; gunakan *serta* untuk relasi penyertaan/pendampingan (makna *beserta*, pelengkap, atau pengikut).
       - **Perincian Bertingkat**: Gunakan *dan* pada perincian kelompok utama, dan *serta* pada kelompok tambahan/sub-rincian (*"A dan B, serta C"*).
       - **Eliminasi Pleonasme**: Larang keras gandeng kata *"dan serta"*.
   - **Unsur Serapan**: Penyesuaian akhiran asing dan konsonan ganda menjadi tunggal.
3. **Penerapan Koreksi Minimal**:
   - Pertahankan struktur kalimat asli dan gaya penulis selama tidak melanggar kaidah EYD V.
4. **Penyajian Hasil**:
   - Sajikan teks bersih secara langsung.
   - Jika pengguna meminta audit atau penjelasan, berikan tabel perbandingan sebelum–sesudah beserta rujukan kaidah atau URL resminya.

## 3. Integrasi Mode DOCX

* Gunakan bersama skill `docx` untuk membaca, menyunting, dan memvalidasi dokumen Microsoft Word.
* Pertahankan format dokumen: gaya paragraf, tabel, catatan kaki (*footnote*), pranala, header/footer, dan pemisah halaman (*page break*).
* Jika pengguna meminta tinjauan (*review*), gunakan fitur perubahan terlacak (*tracked changes*) atau komentar.

## 4. Batas Penyuntingan

* Jangan membakukan dialog karya sastra, slogan, nama produk, atau kutipan langsung kecuali diminta.
* Jangan mengganti istilah teknis hanya karena terasa asing; verifikasi konteksnya.
* Jika EYD V membolehkan variasi (misal: penulisan singkatan/akronim tertentu), pilih satu bentuk yang paling tepat dan terapkan secara konsisten.
