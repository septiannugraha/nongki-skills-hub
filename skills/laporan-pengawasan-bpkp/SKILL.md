---
name: laporan-pengawasan-bpkp
description: Menyusun, mengedit, dan meninjau laporan hasil pengawasan internal (LHP/LHE/LHR) sesuai format BPKP dan standar IIA (Global Internal Audit Standards 15.1). Gunakan saat diminta membuat draf laporan pengawasan, menyunting temuan audit, menyusun simpulan/rekomendasi, atau memvalidasi kelengkapan laporan.
tags: [bpkp, audit, pengawasan, laporan, lhp, lhe, lhr, iia, temuan, rekomendasi]
---

# Laporan Pengawasan BPKP

Skill ini membantu menyusun laporan hasil pengawasan internal (Laporan Hasil Pemeriksaan/LHP, Laporan Hasil Evaluasi/LHE, Laporan Hasil Reviu/LHR) sesuai prinsip Global Internal Audit Standards (IIA Standard 15.1) yang diadaptasi ke dalam konteks BPKP.

Baca [Panduan Standar IIA](references/standar-iia.md) untuk kerangka struktural dan prinsip kualitas komunikasi. Baca [Contoh Struktur Laporan](references/template-format.md) sebagai salah satu contoh format -- bukan format baku (lihat Bagian 2).

## 1. Prinsip Kualitas Komunikasi (IIA)

Setiap teks laporan yang dihasilkan wajib memenuhi 6 karakteristik:

| Prinsip | Penerapan |
|---|---|
| **Akurat** | Data, angka, dan rujukan regulasi harus presisi. Verifikasi setiap angka yang disebut. |
| **Objektif** | Fakta nyata, tanpa opini subjektif. Gunakan "berdasarkan hasil evaluasi..." bukan "menurut kami..." |
| **Jelas** | Bahasa formal Indonesia, hindari jargon yang tidak perlu. Singkatan dieja lengkap pada kemunculan pertama. |
| **Ringkas** | Langsung ke pokok masalah. Satu paragraf = satu ide utama. Hindari pengulangan. |
| **Konstruktif** | Nada membantu perbaikan, bukan menyalahkan. Rekomendasi berorientasi solusi. |
| **Tepat Waktu** | Sajikan informasi yang relevan dengan periode pengawasan yang sedang berjalan. |

## 2. Struktur Dokumen: Tidak Baku, Bervariasi

**PENTING**: Struktur laporan BPKP **tidak baku**. Setiap jenis penugasan (evaluasi, pemeriksaan, reviu, audit kinerja, audit investigasi, dll.) dapat memiliki format dan susunan BAB yang berbeda-beda, tergantung pada:
- Jenis penugasan dan pedoman teknis yang berlaku
- Arahan dari pimpinan/penanggung jawab penugasan
- Template yang sudah disediakan oleh unit kerja

Contoh struktur di [references/template-format.md](references/template-format.md) hanya merupakan **satu contoh** dari jenis Laporan Hasil Evaluasi (LHE). Jangan gunakan contoh tersebut sebagai format wajib untuk semua laporan.

### Pendekatan yang benar:
1. **Jika pengguna memberikan template**: Ikuti template tersebut. Jangan memaksakan struktur dari contoh.
2. **Jika pengguna tidak memberikan template**: Tanyakan jenis penugasan dan apakah ada format/template yang harus diikuti. Jika tidak ada, gunakan contoh di references sebagai titik awal dan sesuaikan.
3. **Yang selalu berlaku di semua jenis laporan**: Kerangka 5C untuk temuan (Bagian 3), prinsip kualitas komunikasi (Bagian 1), distribusi terbatas (Bagian 4), dan conformance statement (Bagian 5).

### Placeholder dan Kertas Kerja

Jika pengguna sudah menyediakan **template laporan** (dalam format DOCX atau format lain), placeholder/variabel yang perlu diisi pada template tersebut **umumnya berasal dari kertas kerja berbentuk xlsx** (spreadsheet). Kertas kerja xlsx biasanya memuat data temuan, angka realisasi, target, bukti audit, dan informasi pendukung lainnya yang perlu dipindahkan ke dalam template laporan.

Skill ini tidak memiliki kemampuan bawaan untuk membaca file xlsx. Jika pengguna perlu mengambil data dari kertas kerja xlsx untuk mengisi placeholder template, gunakan **skill atau alat terpisah** untuk membaca xlsx terlebih dahulu, lalu gunakan data yang diperoleh untuk mengisi template laporan melalui skill ini.

## 3. Kerangka Penulisan Temuan: Metode 5C

Setiap temuan/permasalahan harus diurai menggunakan kerangka 5C. Urutan penulisan dalam laporan BPKP mengikuti pola naratif berikut:

### Pola Naratif Per Sub-Topik

```
[Nomor] [Judul Permasalahan]

[Paragraf Condition -- Kondisi]
Uraikan fakta di lapangan. Berikan data kuantitatif jika tersedia
(tabel, angka, persentase). Gunakan kalimat deklaratif.

[Paragraf Criteria -- Kriteria]
"Kondisi ini tidak sesuai dengan [Regulasi/Peraturan] pasal [X]
yang menyatakan bahwa..."
Kutip pasal/ayat yang relevan secara spesifik.

[Paragraf Cause -- Penyebab]
"Hal ini disebabkan [akar masalah]..."
Identifikasi root cause, bukan sekadar gejala.

[Paragraf Consequence -- Akibat]
"Akibatnya [dampak negatif bagi organisasi/masyarakat]..."
Nyatakan dampak finansial, operasional, atau risiko yang timbul.
```

### Pola Naratif Per Topik (Agregat)

Setelah semua temuan per sub-topik diuraikan, topik ditutup dengan:

```
[Nomor] Risiko yang dapat terjadi dan belum termitigasi terhadap
[topik], antara lain:
a) [Nama Risiko]
   Risiko ini dapat terjadi karena [penyebab ringkas].
b) ...

[Nomor] Terhadap permasalahan tersebut direkomendasikan kepada
[Pejabat] agar:
a) [Rekomendasi strategis -- level Bupati/Gubernur]
b) Menginstruksikan [Kepala OPD] untuk:
   (1) [Rekomendasi taktis 1]
   (2) [Rekomendasi taktis 2]
   ...
```

### Kunci Penulisan 5C dalam Konteks BPKP

- **Criteria**: Selalu kutip regulasi spesifik (UU, PP, Permen, Perda, Perbup, SE, Juknis) beserta pasal dan ayat. Jangan hanya menyebut "sesuai ketentuan" tanpa regulasi eksplisit.
- **Condition**: Nyatakan fakta berbasis bukti audit. Sertakan data kuantitatif (tabel, angka realisasi vs target) bila ada.
- **Cause**: Identifikasi akar masalah (root cause) yang bersifat sistemik, bukan sekadar gejala permukaan.
- **Consequence**: Nyatakan dampak nyata atau risiko potensial. Gunakan kalimat "Akibatnya..." sebagai penanda.
- **Corrective Action / Rekomendasi**: Berjenjang -- rekomendasi strategis untuk pimpinan daerah, rekomendasi taktis/operasional untuk kepala OPD. Harus spesifik dan actionable.

## 4. Distribusi dan Kerahasiaan

Setiap laporan wajib memuat klausul distribusi terbatas:

> "Laporan ini terbatas ditujukan kepada [Jabatan Penerima] untuk dapat digunakan sebagai salah satu bahan pertimbangan atau rekomendasi dalam pengambilan keputusan atas permasalahan yang terjadi."

Tembusan hanya kepada pejabat yang berwenang sesuai hierarki:
- Deputi Kepala BPKP yang relevan
- Pejabat lain sesuai kebutuhan

## 5. Pernyataan Pemenuhan Norma (Conformance Statement)

Laporan wajib memuat pernyataan bahwa pengawasan telah dilakukan sesuai:
1. Standar Audit Intern Pemerintah Indonesia (SAIPI) yang diterbitkan AAIPI
2. Peraturan BPKP tentang Standar Kerja Pengawasan Intern BPKP

Contoh kalimat standar:
> "Pengawasan ini telah dilakukan sesuai Standar Audit Intern Pemerintah Indonesia yang diterbitkan Asosiasi Auditor Intern Pemerintah Indonesia (AAIPI) dan Peraturan BPKP Nomor [X] Tahun [XXXX] tentang Standar Kerja Pengawasan Intern BPKP."

## 6. Konvensi Gaya Penulisan

### Singkatan dan Akronim
- Tulis lengkap pada kemunculan pertama, diikuti singkatan dalam kurung.
  Contoh: "Lahan Pertanian Pangan Berkelanjutan (LP2B)"
- Setelahnya gunakan singkatan secara konsisten.

### Penomoran Bertingkat
Gunakan hierarki berikut (sesuaikan dengan template jika sudah disediakan):
```
1.   (tema utama)
  a.  (sub-tema)
    1)  (sub-sub)
      a)  (butir)
        (1)  (sub-butir)
          (a)  (anak sub-butir)
```

### Nada dan Diksi
- Formal, impersonal: "telah dilakukan evaluasi..." bukan "kami mengevaluasi..."
- Konstruktif: "direkomendasikan agar..." bukan "harus segera dilakukan..."
- Hindari kata-kata emosional atau menghakimi.
- Gunakan kalimat pasif untuk temuan, kalimat aktif untuk rekomendasi.

### Tabel dan Data
- Setiap tabel harus memiliki judul dan sumber data.
- Format: "Sumber: [Nama Instansi/Dokumen], [Tahun]"

---

## 7. Humanisasi Bahasa (Built-In)

Setiap teks laporan yang dihasilkan harus terasa ditulis oleh auditor profesional untuk audiens tertentu (Bupati, Kepala OPD, Deputi), bukan teks yang terasa generik atau mekanis.

### Sasaran
Hasilkan tulisan yang terasa ditulis seseorang untuk audiens tertentu. Pertahankan tingkat formalitas, tujuan, fakta, istilah, kutipan, dan suara penulis. Dalam teks dinas, manusiawi berarti **jernih dan tidak mekanis**, bukan percakapan santai.

### Pola yang Harus Diperiksa dan Dihindari

**Artefak chatbot:**
- Pembuka seperti "Tentu", "Baik", atau "Berikut adalah" ketika teks dapat langsung dimulai.
- Penutup seperti "Semoga bermanfaat" atau tawaran bantuan yang bukan bagian dari naskah.
- Sapaan dan pujian generik yang tidak cocok dengan genre laporan.

**Klaim dan abstraksi:**
- "merupakan bukti nyata", "memainkan peran penting", "menjadi tonggak", "di tengah lanskap yang terus berkembang" tanpa informasi konkret.
- Kata evaluatif seperti "sangat penting", "komprehensif", "inovatif", atau "strategis" tanpa ukuran atau bukti.
- Atribusi kabur: "para ahli mengatakan", "banyak pihak menilai", atau "berbagai penelitian" tanpa sumber.

**Struktur mekanis:**
- Paragraf dengan pola pembuka-tiga butir-kesimpulan yang berulang.
- Setiap bagian diakhiri rangkuman yang hanya mengulang isinya.
- Kalimat berpanjang hampir sama dan selalu memakai pola subjek-predikat-objek.
- Penggunaan "selain itu", "lebih lanjut", "di sisi lain", dan "oleh karena itu" secara beruntun meski hubungan antarkalimat sudah jelas.
- Konstruksi "bukan hanya ..., melainkan juga ..." yang dipakai sebagai hiasan.

### Perbaikan yang Aman
- Ganti abstraksi dengan siapa melakukan apa, jika informasinya memang tersedia.
- Gabungkan kalimat yang mengulang; pecah kalimat yang menanggung terlalu banyak gagasan.
- Pakai kata "adalah", "ialah", "punya", atau verba langsung ketika lebih alami untuk ragam formal.
- Pertahankan istilah resmi, teknis, dan kutipan regulasi. Jangan mengarang contoh, statistik, pengalaman, atau sikap penulis.
- Variasikan panjang serta bentuk kalimat secara wajar. Jangan sengaja menambahkan kesalahan, slang, humor, opini, atau pengalaman pribadi.
- Baca keras secara mental. Hapus kalimat yang terdengar seperti slogan, presentasi korporat, atau respons chatbot.
- Lakukan audit makna: angka, nama, negasi, tingkat kepastian, hubungan sebab-akibat, dan kutipan harus tetap sama.

---

## 8. Pemeriksaan EYD V (Built-In)

Setelah humanisasi, periksa ejaan sesuai kaidah EYD V (Ejaan Bahasa Indonesia yang Disempurnakan Edisi V). DILARANG mengubah nama diri, istilah merek, kutipan langsung regulasi, kode, URL, rumus, atau slogan tanpa instruksi spesifik.

### Pemeriksaan Berurutan

#### A. Penggunaan Huruf

**Huruf Kapital:**
- Jabatan/Gelar: Kapital jika diikuti nama diri (*Presiden Joko Widodo*, *Gubernur Jawa Barat*). Kecil jika tidak diikuti nama (*menjadi seorang presiden*, *calon gubernur*).
- Geografis: Kapital jika spesifik/nama diri (*Danau Toba*, *Kecamatan Menteng*). Kecil jika generik/nama jenis (*berenang di danau*).
- Nama Bangsa/Suku/Bahasa: Kapital (*bahasa Indonesia*, *suku Dayak*).

**Huruf Miring:**
- Istilah/kata asing atau bahasa daerah yang belum diserap (*online*, *drive-thru*).
- Judul buku, majalah, atau surat kabar yang dikutip dalam kalimat.

**Huruf Tebal:**
- Menegaskan bagian tulisan yang sudah dimiringkan, serta judul bab/subbab.

#### B. Penulisan Kata

**Kata Depan vs Imbuhan:**
- Kata Depan (`di`, `ke`, `dari`): Dipisah jika menunjukkan tempat/arah/waktu (*di rumah*, *ke mana*, *dari Surabaya*).
- Imbuhan (`di-`, `ke-`): Disambung jika membentuk kata kerja pasif atau kata bilangan (*ditulis*, *dimakan*, *ketiga*).

**Bentuk Terikat (`pasca-`, `sub-`, `non-`, `anti-`, `antar-`):**
- Disambung dengan kata yang mengikutinya (*pascabencana*, *antarkota*, *nonaktif*).
- Tanda hubung jika diikuti kata berawalan kapital atau angka (*non-Indonesia*, *pro-IKN*).

**Bentuk Terikat `maha-`:**
- Disambung jika diikuti kata dasar mengacu Tuhan (*Mahakuasa*, *Mahatahu*). Pengecualian: *Maha Esa*.
- Dipisah jika diikuti kata berimbuhan (*Maha Pengasih*, *Maha Pemurah*).

**Partikel `pun`:**
- Dipisah jika bermakna "juga" (*apa pun*, *saya pun*, *siapa pun*).
- Disambung pada kata klise: *adapun*, *ataupun*, *bagaimanapun*, *biarpun*, *kalaupun*, *kendatipun*, *maupun*, *meskipun*, *sungguhpun*, *walaupun*, *sekalipun*.

**Singkatan dan Akronim:**
- Singkatan umum 3 huruf kecil diakhiri 1 titik (*dll.*, *dsb.*, *hlm.*, *yth.*).
- Singkatan umum 2 huruf kecil menggunakan titik di tiap huruf (*a.n.*, *d.a.*, *s.d.*, *u.p.*).
- Akronim nama diri menggunakan kapital tanpa titik (*BPKP*, *SAIPI*, *AAIPI*).

**Angka dan Bilangan:**
- Ditulis huruf jika satu atau dua kata (*tiga kali*, *dua puluh orang*).
- Ditulis digit untuk rincian, ukuran, nilai uang, waktu (*5 cm*, *Rp50.000,00*, *pukul 08.00*).

#### C. Penggunaan Tanda Baca

**Tanda Koma (`,`):**
- Sebelum konjungsi pertentangan (*..., tetapi...*, *..., melainkan...*, *..., sedangkan...*).
- Dalam rincian 3+ unsur sebelum "dan"/"atau" (Oxford comma: *A, B, dan C*).
- Di belakang kata transisi antarkalimat (*Oleh karena itu, ...*, *Namun, ...*).
- Anak kalimat mendahului induk kalimat: pakai koma (*Jika hujan, saya tidak datang*). Sebaliknya, tanpa koma.

**Tanda Titik Dua (`:`):**
- Di akhir pernyataan lengkap yang diikuti rincian.
- TIDAK jika rincian merupakan pelengkap langsung kalimat.

**Tanda Hubung (`-`):**
- Kata ulang (*anak-anak*), `ke-` + angka (*ke-2*), angka + `-an` (*tahun 1990-an*), imbuhan + kata asing (*di-upgrading*).

**Tanda Pisah (`--`):**
- Mengapit penyisipan kata/kalimat penjelas.
- Berarti "sampai dengan" di antara bilangan/tanggal.

**Tanda Petik (`"..."`):**
- Mengapit petikan langsung. Titik/koma penutup di **dalam** tanda petik.

#### D. Unsur Serapan

**Penyesuaian Akhiran Asing:**
- *-ism* -> *-isme*, *-ty* -> *-tas*, *-tion* -> *-si*, *-logy* -> *-logi*, *-ive* -> *-if*, *-ic* -> *-ik*

**Konsonan Ganda:**
- Diserap menjadi tunggal (*effect* -> *efek*, *commission* -> *komisi*).

### Verifikasi Kasus Batas

Jika aturan EYD diragukan atau terdapat kata serapan yang berpotensi diperdebatkan, gunakan `webfetch` ke URL spesifik dari situs resmi EYD V:
- Situs utama: <https://ejaan.kemendikdasmen.go.id/eyd/>
- Huruf Kapital: <https://ejaan.kemendikdasmen.go.id/eyd/penggunaan-huruf/huruf-kapital/>
- Kata Depan: <https://ejaan.kemendikdasmen.go.id/eyd/penulisan-kata/kata-depan/>
- Singkatan dan Akronim: <https://ejaan.kemendikdasmen.go.id/eyd/penulisan-kata/singkatan-dan-akronim/>
- Tanda Koma: <https://ejaan.kemendikdasmen.go.id/eyd/penggunaan-tanda-baca/tanda-koma/>
- Unsur Serapan Umum: <https://ejaan.kemendikdasmen.go.id/eyd/unsur-serapan/umum/>
- Unsur Serapan Khusus: <https://ejaan.kemendikdasmen.go.id/eyd/unsur-serapan/khusus/>

### Batas Penyuntingan EYD
- Jangan mengubah kutipan langsung regulasi kecuali diminta.
- Jangan mengganti istilah teknis audit/pemerintahan hanya karena terasa asing; verifikasi konteksnya.
- Jika EYD V membolehkan variasi, pilih satu bentuk dan terapkan secara konsisten di seluruh dokumen.

---

## 9. Alur Kerja (Workflow)

### Langkah 1: Identifikasi Jenis dan Format Laporan
Tanyakan kepada pengguna jika belum jelas:
- Jenis laporan (LHP / LHE / LHR / lainnya)
- Objek pengawasan
- Periode pengawasan
- Perwakilan BPKP pelaksana
- **Apakah sudah ada template laporan yang harus diikuti?** Jika ya, minta template-nya. Jika template memiliki placeholder, tanyakan apakah data pengisinya berasal dari kertas kerja xlsx.

### Langkah 2: Kumpulkan Data
- Minta data temuan, bukti audit, dan regulasi terkait.
- Jika pengguna memberikan data mentah (dari kertas kerja xlsx atau sumber lain), bantu menyusunnya ke dalam kerangka 5C.
- Jika data berasal dari file xlsx, minta pengguna membaca xlsx menggunakan skill/alat terpisah terlebih dahulu, atau berikan data dalam format yang bisa dibaca.

### Langkah 3: Susun Draf
- Jika ada template: ikuti template. Isi placeholder dengan data yang diperoleh.
- Jika tidak ada template: gunakan contoh di references sebagai titik awal, sesuaikan dengan jenis penugasan.
- Untuk setiap temuan, terapkan kerangka 5C (Bagian 3).
- Pastikan simpulan konsisten dengan uraian temuan.
- Pastikan rekomendasi konsisten dengan uraian temuan.

### Langkah 4: Validasi Kelengkapan
Periksa bahwa laporan memuat (sesuaikan dengan jenis laporan):
- [ ] Klausul distribusi terbatas
- [ ] Conformance statement (pernyataan pemenuhan norma)
- [ ] Kerangka 5C untuk setiap temuan (Condition, Criteria, Cause, Consequence)
- [ ] Identifikasi risiko dan rekomendasi per topik
- [ ] Kutipan regulasi lengkap (nama, nomor, tahun, pasal, ayat)
- [ ] Tabel dengan judul dan sumber
- [ ] Singkatan dieja lengkap pada kemunculan pertama
- [ ] Konsistensi antara simpulan dan uraian temuan
- [ ] Konsistensi antara rekomendasi ringkas dan rekomendasi detail

### Langkah 5: Penyuntingan Bahasa
Setelah substansi final, lakukan dua tahap secara berurutan:

1. **Humanisasi bahasa** (Bagian 7):
   - Periksa dan perbaiki kalimat mekanis, struktur berulang, dan artefak chatbot.
   - Pastikan teks terasa ditulis auditor profesional untuk pembaca spesifik.
   - Pertahankan semua fakta, angka, kutipan regulasi, dan istilah teknis.

2. **Pemeriksaan EYD V** (Bagian 8):
   - Periksa huruf kapital, kata depan vs imbuhan, tanda baca, singkatan, dan unsur serapan.
   - Pertahankan istilah teknis audit/pemerintahan yang baku.
   - Verifikasi ke situs resmi EYD V jika ada kasus batas.

### Langkah 6: Pengecekan Akhir
- Pastikan konsistensi penomoran di seluruh dokumen.
- Pastikan konsistensi simpulan - uraian - rekomendasi.
- Laporkan kepada pengguna jika ditemukan inkonsistensi.

## 10. Interaksi dengan Pengguna

- Jika pengguna memberikan data temuan mentah tanpa kerangka 5C, susun ke dalam format 5C dan konfirmasi sebelum finalisasi.
- Jika regulasi yang dikutip pengguna tidak lengkap (tanpa pasal/ayat), tanyakan detailnya.
- Jika diminta menulis satu bagian saja (misal: hanya temuan, hanya rekomendasi), tetap ikuti format yang relevan dari bagian tersebut.
- Jika diminta mengedit laporan yang sudah ada, fokus pada perbaikan substansi (kelengkapan 5C) dan bahasa, tanpa mengubah fakta/data yang sudah ada.
- Jika pengguna memberikan template dengan placeholder, tanyakan sumber data pengisi (umumnya dari kertas kerja xlsx).
