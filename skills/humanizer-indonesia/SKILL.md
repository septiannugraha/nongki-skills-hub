---
name: humanizer-indonesia
description: Rewrite Indonesian text to sound natural, human, specific, and contextually appropriate without changing the original meaning (humanize/naturalization).
tags: [indonesian, humanizer, naturalize, writing, copywriting]
---

# Humanizer Indonesia

## Sasaran

Hasilkan tulisan yang terasa ditulis seseorang untuk audiens tertentu, bukan teks yang sekadar dibuat lebih santai. Pertahankan tingkat formalitas, tujuan, fakta, istilah, kutipan, dan suara penulis.

Baca [pola dan padanan Indonesia](references/pola-bahasa-indonesia.md) sebelum mengerjakan teks panjang atau teks yang sangat terasa seperti keluaran AI.

## Alur kerja

1. Kenali jenis teks, audiens, hubungan penulis–pembaca, nada, dan batas panjang.
2. Tandai ciri mekanis: pembuka generik, klaim besar tanpa bukti, abstraksi berlebihan, daftar tiga serangkai yang dipaksakan, sinonim bergilir, pengulangan kesimpulan, transisi kaku, dan kalimat dengan irama seragam.
3. Tulis ulang hanya bagian yang membutuhkan perubahan. Gunakan kata konkret, subjek yang jelas, verba langsung, dan detail yang tersedia dalam sumber.
4. Variasikan panjang serta bentuk kalimat secara wajar. Jangan sengaja menambahkan kesalahan, slang, humor, opini, atau pengalaman pribadi yang tidak berasal dari penulis.
5. Baca keras secara mental. Hapus kalimat yang terdengar seperti slogan, presentasi korporat, atau respons chatbot.
6. Lakukan audit makna: angka, nama, negasi, tingkat kepastian, hubungan sebab-akibat, dan kutipan harus tetap sama.
7. Jika pengguna juga meminta ejaan baku, jalankan pemeriksaan dengan skill `eyd-indonesia` setelah humanisasi.

## Pilihan keluaran

- Secara default, berikan versi akhir saja.
- Jika diminta transparansi, berikan versi akhir dan ringkasan perubahan utama; jangan membebani pengguna dengan seluruh proses internal.
- Jika ada bagian yang tidak dapat dinaturalisasi tanpa mengubah maksud, pertahankan bagian itu dan beri catatan singkat.

## Mode DOCX

Gunakan bersama skill `docx` atau `editor-docx-indonesia`. Pertahankan format dokumen dan ubah hanya isi yang disetujui. Jangan mengubah kutipan, bibliografi, tabel data, rumus, kode, atau metadata secara otomatis.
