---
name: laporan-pengawasan-bpkp
description: Menyusun dan mengedit laporan hasil pengawasan internal di lingkungan BPKP (LHP, LHE, LHR) berdasarkan Global Internal Audit Standards (IIA Standard 15.1), termasuk kerangka temuan 5C (kondisi, kriteria, sebab, akibat, rekomendasi), prinsip kualitas komunikasi IIA, conformance statement, dan distribusi laporan. Gunakan saat diminta membuat draf laporan hasil pemeriksaan/evaluasi/reviu, menyusun atau memperbaiki bab temuan dan rekomendasi, atau mengisi template laporan dari kertas kerja.
tags: [bpkp, laporan-pengawasan, lhp, lhe, lhr, temuan-audit, 5c, iia, audit-internal]
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

## 3. Kerangka Penulisan Temuan: Metode 5C & Multi-Lokus

Setiap temuan/permasalahan harus diurai menggunakan kerangka 5C. Dalam pengawasan kewilayahan/multi-entitas (misalnya tingkat Provinsi dan beberapa Kabupaten/Kota), uraian temuan mengikuti pola agregat dan rincian per lokus berikut:

### Pola Naratif Per Sub-Topik (Format Multi-Lokus)

```
[a./b./c.] [Judul Permasalahan Spesifik] (Bold 12pt)

Kondisi di tingkat wilayah pengawasan diuraikan sebagai berikut:

1) [Nama Entitas/Provinsi]: [Uraian fakta kondisi riil, data kuantitatif, target vs realisasi, temuan lapangan].
2) [Nama Entitas/Kabupaten A]: [Uraian fakta kondisi riil, data kuantitatif, target vs realisasi, temuan lapangan].
3) [Nama Entitas/Kabupaten B]: [Uraian fakta kondisi riil, data kuantitatif, target vs realisasi, temuan lapangan].

[Kriteria / Regulasi]
(.)  <-- Warna MERAH jika masih berupa draf/placeholder/unverified
-- ATAU --
"Kondisi tersebut tidak sesuai dengan [Regulasi/Peraturan] Nomor [X] Tahun [XXXX] tentang [Judul], Pasal [X] ayat ([X]) yang menyatakan bahwa '[Kutipan normatif]'." (Warna HITAM jika sudah definitif)

[Penyebab / Root Cause]
Kondisi tersebut disebabkan oleh [akar masalah sistemik, bukan sekadar gejala permukaan].

[Akibat / Dampak / Risiko]
Akibatnya, [dampak negatif riil atau potensi risiko finansial/operasional/kegagalan target].

[Rekomendasi / Corrective Action]
Atas permasalahan tersebut, direkomendasikan agar:
1) [Rekomendasi untuk level Provinsi / Pimpinan Daerah];
2) [Rekomendasi untuk level Kabupaten / OPD Teknis].
```

### Pola Naratif Per Topik Utama (Agregat)

Sebelum masuk ke sub-topik `a.`, `b.`, dst., diawali dengan:
```
[Heading 3] [Nomor & Judul Topik Utama] (misal: 1. Lahan Pertanian Belum Terkelola dengan Efektif)

[Paragraf Simpulan Umum Topik]
Uraikan gambaran umum kondisi menyeluruh pada topik tersebut di seluruh wilayah pengawasan secara ringkas dan padat.
```

Setelah seluruh sub-topik temuan selesai, topik ditutup dengan bagian **Tanggapan Mitra Evaluasi dan Rencana Aksi**:
```
Tanggapan Mitra Evaluasi dan Rencana Aksi
Atas hasil evaluasi yang telah disampaikan, pihak [Pemerintah Daerah / OPD terkait] menyatakan sependapat dan berkomitmen menyusun rencana aksi penyelesaian tindak lanjut dengan rincian:
1) [Uraian rencana aksi 1] diselesaikan paling lambat [Bulan/Tahun];
2) [Uraian rencana aksi 2] diselesaikan paling lambat [Bulan/Tahun].
```

### Kunci Penulisan 5C dalam Konteks BPKP

- **Criteria**: Selalu kutip regulasi spesifik (UU, PP, Permen, Perda, Perbup, SE, Juknis) beserta pasal dan ayat. Tandai warna **MERAH (`RGB(255, 0, 0)`)** bila masih placeholder `(.)` atau butuh verifikasi regulasi.
- **Condition**: Nyatakan fakta berbasis bukti KKE (Kertas Kerja Evaluasi). Sajikan perbandingan target vs realisasi atau tabel pendukung bila tersedia.
- **Cause**: Identifikasi akar masalah (*root cause*) dengan awalan baku: `"Kondisi tersebut disebabkan oleh..."`.
- **Consequence**: Nyatakan dampak nyata atau risiko potensial dengan awalan baku: `"Akibatnya, ..."`.
- **Corrective Action / Rekomendasi**: Berjenjang (strategis untuk Kepala Daerah, operasional untuk Kepala OPD) dengan awalan baku: `"Atas permasalahan tersebut, direkomendasikan agar: ..."`.

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
A.   (bagian utama: Simpulan, Rekomendasi, dll.)
  1.  (topik utama: Lahan, Bibit, Pupuk, dll.)
    a.  (sub-temuan spesifik)
      1)  (rincian per lokus/entitas)
        a)  (detail butir)
```

#### Sistem Multilevel Numbering Word (`numbering.xml` / `w:numPr`)

Untuk dokumen yang dibangun dari nol atau tanpa template numbering bawaan, gunakan sistem multilevel list Word native sebagai berikut:

| Level (`ilvl`) | Format | `numFmt` | Contoh | Fungsi |
|---|---|---|---|---|
| 0 | `%1.` | `upperLetter` | **A.** | Heading 2 -- Bagian (Simpulan, Rekomendasi, Hasil Evaluasi) |
| 1 | `%2.` | `decimal` | **1.** | Heading 3 -- Topik utama (Lahan, Bibit, Pupuk, dst.) |
| 2 | `%3.` | `lowerLetter` | **a.** | Sub-Heading temuan spesifik (Bold, bukan style Heading) |
| 3 | `%4)` | `decimal` | **1)** | Rincian per lokus/entitas (Provinsi, Kabupaten) |
| 4 | `%5)` | `lowerLetter` | **a)** | Detail butir/rincian sub-lokus |

**Aturan Restart (`w:lvlOverride` / `w:startOverride`):**
- **Bab baru (Heading 1):** Buat instance `<w:num>` baru dengan `lvlOverride startOverride=1` pada **semua level** (0–4). Seluruh penomoran reset dari A./1./a./1)/a).
- **Topik baru (Heading 3):** Tidak membuat instance baru — topik berbagi `numId` milik Bab. Nomor topik berlanjut sekuensial (1., 2., ..., 10.). Sub-level (a., 1), a)) otomatis restart saat level atas maju, sesuai perilaku bawaan Word multilevel list.
- **Sub-temuan baru (ilvl 2):** Saat `a.` maju ke `b.`, level 3 dan 4 otomatis restart.
- **Locus baru (ilvl 3):** Saat `1)` maju ke `2)`, level 4 otomatis restart.

**Penting tentang `w:rPr` pada `w:lvl`:** Setiap level dalam `abstractNum` wajib menyertakan `<w:rPr>` dengan `<w:rFonts w:ascii="Arial" w:hAnsi="Arial" w:cs="Arial"/>` dan `<w:sz w:val="24"/>` (12 pt) untuk memastikan karakter nomor/letter memakai font Arial 12 pt yang konsisten.

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
- Terapkan ketentuan tata naskah dinas laporan (Bagian 11): bentuk surat/bab, penomoran LHP/LPP, cover, dan penanda tangan sesuai wewenang.
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
- [ ] Penomoran memakai kode `LHP`/`LPP` sesuai format TND (Bagian 11.4)
- [ ] Penanda tangan sesuai wewenang: kepala unit kerja/Pejabat Berwenang untuk laporan hasil pengawasan; kepala unit kerja/Plh. untuk laporan berkala penunjang (Bagian 11.2)
- [ ] Cover memenuhi spesifikasi logo BPKP 3,4 x 1,7 cm, Arial 13-bold lembaga, nama unit kerja kapital Arial 12-bold (Bagian 11.6), bila laporan dicetak bercover

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

---

## 11. Ketentuan Tata Naskah Dinas untuk Laporan (Perban 4/2022)

Bagian ini built-in dari Peraturan BPKP Nomor 4 Tahun 2022 tentang Pedoman Tata Naskah Dinas (Lampiran BAB II bagian Laporan dan BAB III). Berlaku untuk semua laporan yang dihasilkan dalam penugasan pengawasan.

### 11.1 Pengelompokan Laporan

**a. Laporan hasil pengawasan**, antara lain:
1) Laporan Audit Operasional
2) Laporan Audit Kinerja
3) Laporan Audit Untuk Tujuan Tertentu
4) Laporan Audit Investigatif
5) Laporan Audit Penghitungan Kerugian Keuangan Negara
6) Laporan Keterangan Ahli
7) Laporan Evaluasi Hambatan Kelancaran Pembangunan
8) Laporan Reviu
9) Laporan Pemantauan/Monitoring
10) Laporan Bimtek/Asistensi
11) Laporan Sosialisasi
12) Laporan Hasil Kajian
13) Laporan Pembinaan Penyelenggaraan SPIP
14) Laporan Manajemen Risiko/Penilaian Risiko
15) Laporan Kegiatan Good Corporate Governance (GCG)
16) Laporan Pembinaan Peningkatan Kapabilitas APIP
17) Laporan Pembinaan Jabatan Fungsional Auditor
18) Laporan Hasil Pengawasan dan Pembinaan (Presiden/Menteri/Gubernur/Bupati/Walikota)

**b. Laporan penunjang pengawasan**, antara lain:
1) Laporan Monitoring Tindak Lanjut Pengawasan
2) Laporan Kinerja
3) Laporan Realisasi Anggaran
4) Laporan Pelatihan di Kantor Sendiri
5) Laporan Gerakan Disiplin Nasional
6) Laporan SABMN
7) Laporan Penghematan Energi
8) Laporan Kehumasan
9) Laporan Reformasi Birokrasi
10) Laporan Penyelenggaraan SPIP
11) Laporan Budaya Kerja
12) Laporan Pelaksanaan Kegiatan

### 11.2 Wewenang Penciptaan dan Penandatanganan

| Jenis laporan | Penanda tangan |
|---|---|
| Laporan hasil pengawasan | Kepala unit kerja atau Pejabat yang Berwenang |
| Laporan berkala penunjang pengawasan | Kepala unit kerja atau pelaksana harian (Plh.) kepala unit kerja |

### 11.3 Bentuk dan Susunan

- Laporan hasil pengawasan maupun penunjang pengawasan dapat disusun **dalam bentuk surat maupun bentuk bab** sesuai kebutuhan.
- Susunan rinci laporan diatur dalam **pedoman khusus unit kerja teknis terkait**, sepanjang belum diatur oleh unit kerja yang lebih tinggi kedudukannya -- konsisten dengan prinsip "struktur tidak baku" pada Bagian 2 skill ini.

### 11.4 Penomoran Laporan

Laporan menggunakan kode jenis naskah dinas pada nomor:
- `LHP` -- Laporan Hasil Pengawasan
- `LPP` -- Laporan Penunjang Pengawasan

Format nomor mengikuti pola umum TND: `[kode keamanan]/[kode klasifikasi arsip]/[LHP|LPP]/[nomor urut]/[kode konseptor]/[tahun]`. Nomor urut agenda dimulai dari 1 setiap awal tahun. Khusus naskah peraturan tidak memakai pola ini, tetapi laporan tetap memakai pola lengkap.

### 11.5 Distribusi Laporan

- Laporan didistribusikan kepada **pihak yang berkepentingan** dan dapat berupa softcopy yang **disertai surat pengantar**.
- Distribusi tetap tunduk pada prinsip distribusi terbatas (Bagian 4) dan klasifikasi keamanan: Sangat Rahasia (`SR`), Rahasia (`R`), Terbatas (`T`), Biasa (tanpa kode).

### 11.6 Sampul/Cover Laporan

1. Kertas hard cover jenis **buffalo** atau kertas lain dengan spesifikasi lebih tinggi sesuai keperluan.
2. Margin cover mengikuti aturan penyusunan naskah dinas dan estetika.
3. Susunan cover:
   a. **Logo BPKP berwarna** di bagian atas secara simetris; ukuran panjang **3,4 cm**, tinggi **1,7 cm** (proporsi 2:1);
   b. Tulisan **"BADAN PENGAWASAN KEUANGAN DAN PEMBANGUNAN"** (font **Arial 13-bold**) simetris di bawah logo;
   c. **Nama unit kerja** seluruhnya huruf kapital (**Arial 12-bold**) simetris di bawah tulisan lembaga;
   d. **Judul laporan** bebas menggunakan huruf kapital, kursif, font, ukuran, dan warna yang mendukung estetika;
   e. **Nomor dan tanggal laporan** juga boleh divariasikan untuk estetika.

### 11.7 Media Penyajian Visual

1. Untuk stakeholder dengan tujuan tertentu, laporan boleh disajikan dengan media visual (desain grafis, infografis) dalam format berbeda dari tata naskah dinas.
2. Format berbeda tersebut **tetap wajib** memuat: logo dan nama BPKP, nomor naskah dinas, dan pejabat penanda tangan, dengan memperhatikan estetika dan etika.
3. Warna sampul, gambar, dan infografis ditentukan masing-masing unit kerja dengan tetap memperhatikan etika penyajian informasi.

### 11.8 Unsur Pokok Naskah Dinas (untuk laporan bentuk surat)

Kop naskah dinas; nomor; lampiran; hal/perihal; tanggal; alamat tujuan; salam pembuka; isi (pembuka--inti--penutup); salam penutup; nama jabatan penanda tangan; nama pejabat; pangkat dan NIP; tembusan (bila ada); tanda tangan dan nama terang; nomor halaman; lampiran.

---

## 12. Standar Formatting, Indentasi, & Tata Naskah Dinas Word (docx)

Berdasarkan praktik terbaik dan standardisasi penyusunan laporan pengawasan (LHE/LHP) BPKP, berikut adalah aturan teknis formatting, hierarki indentasi, tabel, dan tipografi Word (docx) yang wajib dipatuhi:

### 12.1 Pengaturan Halaman & Tipografi
- **Ukuran Kertas & Margin:** Kertas A4 (21,0 cm x 29,7 cm). Margin Kiri: 3,0 cm (1.18", ruang jilid); Margin Atas, Kanan, dan Bawah: 2,0 cm (0.79").
- **Font:** Wajib menggunakan font **Arial** 100% konsisten di seluruh elemen (heading, paragraf, tabel, nomor, header, footer). Pada OpenXML Word pastikan seluruh *runs* menyertakan:
  `<w:rFonts w:ascii="Arial" w:hAnsi="Arial" w:cs="Arial" w:eastAsia="Arial"/>`
- **Ukuran Font:**
  - Judul Cover Utama: Arial 14–16 pt Bold
  - Tulisan Lembaga Cover: "BADAN PENGAWASAN KEUANGAN DAN PEMBANGUNAN" Arial 13 pt Bold, Nama Perwakilan/Deputi Arial 12 pt Bold
  - Judul BAB (`Heading 1`): Arial 12 pt Bold, Rata Tengah (Center), Spasi Atas 12 pt, Spasi Bawah 6 pt
  - Bagian BAB (`Heading 2` & `Heading 3`): Arial 12 pt Bold, Rata Kiri, Spasi Atas 12 pt, Spasi Bawah 6 pt
  - Sub-Heading Temuan (`a.`, `b.`, dst.): Arial 12 pt Bold
  - Isi Paragraf / Narasi 5C / Rincian / Nama Lokus: Arial 12 pt Regular
  - Header & Isi Tabel: Arial 10 pt (Header Bold, Isi Regular)
  - Catatan Kaki, Keterangan Sumber Tabel, Alamat Kop: Arial 9 pt Regular / Italic
- **Spasi & Perataan:**
  - Line Spacing: **1,15 line pitch** (`w:line="276" w:lineRule="auto"`).
  - Space After: **6 pt** (`w:after="120"` dxa) untuk paragraf umum; Space Before: **0 pt** (kecuali sub-heading temuan: Space Before **8 pt**, dan paragraf nama lokus: Space After **2 pt**).
  - Alignment: **100% Justified (Rata Kiri-Kanan)** untuk seluruh teks narasi, deskripsi kondisi multi-lokus, kriteria, sebab, akibat, rekomendasi, dan simpulan.

---

### 12.2 Headings: Style Word vs Paragraf Biasa

Pemisahan tajuk yang memakai *style Heading* bawaan Word versus tajuk berbentuk paragraf biasa Bold sangat penting untuk mencegah pencemaran Daftar Isi dan Navigation Panel.

| Elemen | Memakai Style Heading Word? | Style / Format | Ukuran Font | Perataan | Muncul di Navigation Panel / TOC? |
|---|---|---|---|---|---|
| **Judul BAB** (mis. `BAB I SIMPULAN DAN REKOMENDASI`) | Ya — `Heading 1` | Bold | 12 pt | Center | Ya |
| **Bagian BAB** (mis. `A. Simpulan`, `B. Rekomendasi`) | Ya — `Heading 2` | Bold | 12 pt | Left | Ya |
| **Topik Utama** (mis. `1. Lahan Pertanian Belum Terkelola...`) | Ya — `Heading 3` | Bold | 12 pt | Left | Ya |
| **Sub-Heading Temuan** (mis. `a. Penetapan LP2B Belum...`) | **TIDAK** — paragraf biasa | Bold | 12 pt | Justify/Left | **TIDAK** |
| **Judul bagian non-temuan** (mis. `Tanggapan Mitra Evaluasi dan Rencana Aksi`) | **TIDAK** — paragraf biasa | Bold | 12 pt | Left | **TIDAK** |

**Aturan Bold pada Heading & Sub-Heading:**
- **Heading 1/2/3 (style Word):** Bold 12 pt — seluruh teks tajuk termasuk nomor otomatis adalah Bold.
- **Sub-Heading Temuan (`a.`, `b.`):** Bold 12 pt — **seluruh teks** pada paragraf tersebut (nomor + judul) adalah Bold. Jangan mencampur Bold dan Regular dalam satu baris sub-heading.
- **Paragraf narasi 5C (Kondisi, Kriteria, Sebab, Akibat, Rekomendasi):** **Regular 12 pt** — tidak ada Bold.
- **Nama Lokus pada rincian multi-lokus:** **Regular 12 pt** — tidak di-Bold. Nama lokus berdiri sebagai sub-heading bernomor pada paragraf tersendiri, diikuti narasi pada paragraf terpisah di bawahnya (lihat Bagian 12.6 dan 12.7).
- **Judul Butir pada detail item (`a)`):** **Bold 12 pt** — hanya judul butir yang Bold; titik dua dan isi Regular.

> **Catatan pengalaman:** Spesifikasi awal (`file.md`) menetapkan teks isi 11 pt dan heading 12 pt. Namun dalam implementasi kode, seluruh teks diseragamkan menjadi **12 pt** untuk konsistensi dan kesederhanaan. Standar 12 pt seragam ini yang digunakan sebagai acuan praktis.

### 12.3 Sistem Tab Stop & Hierarki Indentasi Presisi (Hanging Indent Cascade)

Sistem indentasi menggunakan prinsip **cascade**: posisi nomor setiap level berhimpit (sejajar) dengan posisi awal teks pada level di atasnya. Jarak antar level = 360 dxa (0,25"). Formula ini memastikan hierarki visual yang konsisten dan mencegah kerusakan tata letak saat kalimat terbungkus ke baris kedua (*line wrapping*).

#### Formula Cascade (dxa = twips, 1440 dxa = 1 inci)

| `ilvl` | Format | Nomor di (dxa) | Teks di (dxa) | `w:ind w:left` | `w:ind w:hanging` | `w:tab w:pos` |
|---|---|---|---|---|---|---|
| 0 | `A.` | 360 | 720 | 720 | 360 | 720 |
| 1 | `1.` | 720 | 1080 | 1080 | 360 | 1080 |
| 2 | `a.` | 1080 | 1440 | 1440 | 360 | 1440 |
| 3 | `1)` | 1440 | 1800 | 1800 | 360 | 1800 |
| 4 | `a)` | 1800 | 2160 | 2160 | 360 | 2160 |

> **Konversi ke inci:** 360 dxa = 0,25" | 720 = 0,50" | 1080 = 0,75" | 1440 = 1,00" | 1800 = 1,25" | 2160 = 1,50"

#### Penempatan Level pada Konteks Laporan

| Level / Elemen | `ilvl` | Left Indent | First Line (Hanging) | Tab Stop | Perataan & Gaya Font |
|---|---|---|---|---|---|
| **Topik Utama (`Heading 3`)** | 1 | `0,50"` (720 dxa) | `-0,25"` (-360 dxa) | `720 dxa` | Left, Arial 12 pt Bold |
| **Simpulan Topik** (paragraf pembuka) | — | `0,50"` (720 dxa) | `0,00"` | — | Justified, Arial 12 pt Regular |
| **Sub-Heading Temuan** (`a.`, `b.`) | 2 | `0,75"` (1080 dxa) | `-0,25"` (-360 dxa) | `1080 dxa` | Justified, Arial 12 pt **Bold** |
| **Pengantar Kondisi** ("Kondisi di tingkat...") | — | `0,75"` (1080 dxa) | `0,00"` | — | Justified, Arial 12 pt Regular |
| **Rincian Lokus** (`1)`, `2)`) | 3 | `1,00"` (1440 dxa) | `-0,25"` (-360 dxa) | `1440 dxa` | Justified, Arial 12 pt Regular |
| **Detail Item** (`a)`, `b)`) | 4 | `1,25"` (1800 dxa) | `-0,25"` (-360 dxa) | `1800 dxa` | Justified, Arial 12 pt Regular |
| **Kriteria / Penyebab / Akibat / Rekomendasi** | — | `1,25"` (1800 dxa) | `0,00"` | — | Justified, Arial 12 pt Regular |

#### Body Paragraf di Bawah Level Bernomor
Paragraf narasi 5C (Kriteria, Penyebab, Akibat, Rekomendasi) menggunakan **Left Indent = posisi teks level 3** (`1,25"` / 1800 dxa), **bukan** level 2. Ini sejajar dengan posisi teks rincian lokus (`1)`), karena dalam implementasi kode, fungsi `add_criteria()`, `add_cause()`, `add_effect()` menerima parameter `ilvl=3` dan mengambil `left` dari `_LEVEL_FMT[3]` yang bernilai 1800 dxa. Dengan demikian:
- Paragraf pengantar kondisi ("Kondisi di tingkat...") → Left `0,75"` (1080 dxa), sejajar dengan teks sub-heading `a.` (dari `add_body_sub` dengan `ilvl=2`)
- Paragraf Kriteria, Penyebab, Akibat, Rekomendasi → Left `1,25"` (1800 dxa), sejajar dengan teks rincian lokus `1)` (dari `add_criteria`/`add_cause`/`add_effect` dengan `ilvl=3`)

#### Rincian Lokus: Dua-Paragraf Terpisah (Mode Numbering Otomatis)

Pada mode numbering otomatis, rincian per lokus (`1)`, `2)`, `3)`) dipecah menjadi **dua paragraf terpisah**:
1. **Paragraf nama lokus (sub-heading bernomor):** Hanya berisi nama lokus (mis. `Provinsi Papua Tengah`), tanpa titik dua, tanpa narasi. Format: **Regular** (tidak Bold), 12 pt, Spasi After **2 pt** (lebih kecil dari default 6 pt, untuk merapatkan jarak ke narasi).
2. **Paragraf narasi lokus:** Berisi uraian fakta kondisi riil. Left Indent sejajar dengan teks level 3 (`1,25"` / 1800 dxa). Format: Regular 12 pt, Spasi After 6 pt.

Contoh struktur:
```
1)  Provinsi Papua Tengah          ← paragraf 1: nama lokus, Regular, spasi after 2pt
    Pemerintah Provinsi Papua Tengah belum menetapkan Perda maupun Pergub mengenai LP2B...  ← paragraf 2: narasi
2)  Kabupaten Nabire               ← paragraf 1: nama lokus
    Peraturan Daerah tentang RTRW Kabupaten Nabire belum ditetapkan...  ← paragraf 2: narasi
```

> **Pada mode manual (legacy/fallback):** Nama lokus, titik dua, dan narasi disatukan dalam satu paragraf: `1)\t[Nama Lokus]**:** [Narasi]` dengan nama lokus Bold. Mode otomatis lebih disukai karena menghasilkan struktur yang lebih bersih dan rapi.

---

### 12.4 Standar Format Tabel BPKP (Clean Open-Table Style)

Tabel dalam laporan BPKP disajikan secara bersih, rapi, dan profesional dengan kaidah:
- **Borders:** Hanya menggunakan garis horizontal (Top, Bottom, dan garis pemisah header) tipis single border (`sz="4"`, warna abu-abu `#B0B0B0` atau hitam `#000000`). **DILARANG menggunakan border vertikal** (Left, Right, InsideV diset `val="none"`).
- **Cell Padding (Margin Sel):** Top/Bottom: 100 dxa (~5 pt), Left/Right: 150 dxa (~7.5 pt) agar teks tidak menempel ketat pada garis border.
- **Header Baris:** Background shading abu-abu muda (`#F2F2F2` atau `#E6E6E6`), Font Arial 10 pt Bold, Center/Left aligned, Vertically centered.
- **Isi Tabel:** Font Arial 10 pt Regular. Kolom Angka/Realisasi rata kanan (*Right-aligned*), Kolom No rata tengah (*Center*), Kolom Uraian rata kiri/justified.
- **Keterangan Sumber:** Wajib dicantumkan di bawah tabel dengan format: *Sumber: [Nama Instansi / Kertas Kerja Evaluasi], [Tahun]* (Font Arial 9 pt Italic).

---

### 12.5 Aturan Pewarnaan Font Teks & Placeholder
- **Warna MERAH (`RGB(255, 0, 0)`):** Digunakan secara khusus untuk kalimat, kata, atau paragraf yang memuat placeholder **`(.)`**, kriteria yang belum diverifikasi, atau data yang masih membutuhkan konfirmasi/draf.
- **Warna HITAM (`RGB(0, 0, 0)`):** Digunakan untuk seluruh teks/paragraf yang sudah definitif, *fixed*, dan terverifikasi dari bukti/kertas kerja pengawasan.

### 12.6 Aturan Titik Dua (`:`)

Tanda titik dua (`:`) memiliki tiga konteks penggunaan utama dalam laporan pengawasan BPKP, masing-masing dengan aturan format yang berbeda:

#### A. Titik Dua pada Metadata Kop Surat
Pada blok metadata surat pengantar (Nomor, Lampiran, Hal, Tanggal), titik dua **diletakkan tepat setelah label** tanpa spasi sebelum, lalu **satu spasi** sebelum nilai:
```
Nomor    : PE.09.03/LHP-314/PW36/2/2026
Lampiran : Satu Berkas
Hal      : Laporan Hasil Evaluasi atas Tata Kelola...
```
Label rata kiri dengan padding tetap (mis. `Nomor` + spasi = 10 karakter), lalu `:`, lalu spasi, lalu nilai. Titik dua pada baris tanggal tidak digunakan (tanggal ditulis langsung).

#### B. Titik Dua pada Pengantar Daftar Bernomor
Kalimat pengantar yang diikuti daftar bernomor **wajib diakhiri titik dua** (bukan titik atau koma):
- `Kondisi di tingkat wilayah pengawasan diuraikan sebagai berikut:`
- `Atas permasalahan tersebut, direkomendasikan agar:`
- `...menyatakan sependapat dan berkomitmen menyusun rencana aksi penyelesaian tindak lanjut dengan rincian:`

Setelah titik dua, baris berikutnya langsung berisi butir daftar bernomor. Tidak boleh ada teks tambahan setelah titik dua pada baris yang sama.

#### C. Titik Dua pada Label Nama Lokus
Pada mode numbering otomatis, nama lokus **tidak menggunakan titik dua** — nama lokus berdiri sebagai sub-heading bernomor pada paragraf tersendiri (Regular, tanpa Bold, tanpa titik dua), dan narasi mengikuti pada paragraf terpisah di bawahnya.

Pada mode manual (legacy/fallback), nama lokus diikuti titik dua lalu spasi sebelum narasi dalam satu paragraf yang sama. Nama lokus **Bold**, titik dua dan narasi **Regular**:
```
1) Provinsi Papua Tengah: [narasi kondisi riil...]
2) Kabupaten Nabire: [narasi kondisi riil...]
```
Format mode manual: `[Nomor Manual]\t[Nama Lokus]**:** [Narasi Regular]`. Titik dua langsung menempel setelah nama lokus tanpa spasi sebelum, lalu satu spasi sebelum narasi.

> **Mode otomatis lebih disukai** karena menghasilkan struktur yang lebih bersih: nama lokus sebagai paragraf bernomor tersendiri, narasi sebagai paragraf terpisah di bawahnya, tanpa titik dua.

#### D. Titik Dua pada Sumber Tabel
Format keterangan sumber data di bawah tabel menggunakan titik dua setelah kata "Sumber":
```
Sumber: Dinas Pertanian Kabupaten Nabire diolah, 2026
```
Dicetak miring (*Italic*), Arial 9 pt, tanpa indentasi.

#### E. Titik Dua pada Detail Item Bernomor
Pada baris detail item (`a)`, `b)`) yang memiliki judul butir, format: `[Nomor Otomatis]\t[Judul Butir]**:** [Isi Regular]`. Titik dua menempel setelah judul butir tanpa spasi sebelum, lalu satu spasi sebelum isi.

### 12.7 Aturan Huruf Cetak Bold (Bold Font)

Bold hanya digunakan untuk elemen struktural dan penanda, **bukan** untuk menonjolkan kata atau frasa dalam narasi body. Aturan rinci:

| Elemen | Bold? | Ukuran | Keterangan |
|---|---|---|---|
| Heading 1 (Judul BAB) | Ya | 12 pt | Seluruh teks tajuk |
| Heading 2 (Bagian BAB) | Ya | 12 pt | Seluruh teks tajuk |
| Heading 3 (Topik Utama) | Ya | 12 pt | Seluruh teks tajuk |
| Sub-Heading Temuan (`a.`, `b.`) | Ya | 12 pt | Seluruh teks: nomor + judul |
| Judul Bagian Non-Temuan (mis. "Tanggapan Mitra Evaluasi...") | Ya | 12 pt | Seluruh teks tajuk |
| Nama Lokus pada rincian (`Provinsi Papua Tengah`) | **TIDAK** | 12 pt | Regular — nama lokus berdiri sebagai sub-heading bernomor pada paragraf tersendiri (mode otomatis) |
| Judul Butir pada detail item (`Risiko:`) | Ya | 12 pt | Hanya judul butir yang Bold; titik dua dan isi Regular |
| Label Metadata Kop (`Nomor`, `Lampiran`, `Hal`) | Tidak | 12 pt | Regular; nilai juga Regular |
| Paragraf Narasi 5C (Kondisi, Kriteria, Sebab, Akibat, Rekomendasi) | **TIDAK** | 12 pt | 100% Regular, tanpa Bold |
| Awalan baku 5C ("Kondisi tersebut disebabkan oleh...", "Akibatnya,...") | **TIDAK** | 12 pt | Regular — bukan Bold |
| Isi Tabel Header | Ya | 10 pt | Header baris bold |
| Isi Tabel Body | Tidak | 10 pt | Regular |
| Nomor Halaman, Footer | Tidak | 9 pt | Regular |

**Larangan Bold:**
- DILARANG mem-BeBold kata atau frasa di tengah paragraf narasi untuk penekanan (mis. "**sangat** penting", "**belum** sesuai"). Penekanan dalam laporan dinas dilakukan melalui diksi tegas, bukan format.
- DILARANG mem-BeBold seluruh paragraf narasi (kecuali memang berfungsi sebagai sub-heading temuan).
- DILARANG mencampur Bold dan Regular dalam satu baris sub-heading temuan — seluruh baris harus Bold.
- DILARANG mem-BeBold nama lokus pada mode numbering otomatis — nama lokus adalah Regular dan berdiri sebagai paragraf tersendiri.

> **Catatan ukuran font:** Spesifikasi awal proyek menetapkan teks isi 11 pt dan heading 12 pt. Namun dalam implementasi kode aktual, seluruh teks (heading, sub-heading, body, narasi 5C, nama lokus) diseragamkan menjadi **12 pt** untuk konsistensi. Hanya tabel (10 pt) dan catatan kaki/sumber (9 pt) yang berbeda.

---

### 12.8 Penomoran Word Otomatis vs Penomoran Manual
- **Penomoran Otomatis Word Native:** Seluruh elemen penomoran otomatis Word (`w:numPr`, `numbering.xml`), hirarki *list level*, tabulasi, dan *indentation* asli dari template harus dipergunakan dan dipertahankan.
- **Fallback Standar Penomoran & Indentasi:** Apabila draf/template laporan tidak memiliki hirarki *list level*, tabulasi, dan *indentation* bawaan, gunakan formula cascade hanging indent & tab stops Bagian 12.3 atau sistem multilevel numbering Bagian 6 (Penomoran Bertingkat).
- **Larangan Penomoran Teks Ganda (*Double Numbering*):** DILARANG keras mengetik nomor manual teks (seperti `1. `, `a. `, `1) `) di dalam teks paragraf yang bertabrakan dengan penomoran otomatis Word (`w:numPr`). Jika paragraf sudah memiliki `w:numPr`, biarkan Word yang menghasilkan nomor. Jika menggunakan penomoran manual (legacy/fallback), jangan gunakan `w:numPr` pada paragraf yang sama.
- **Format Nomor Manual (Fallback):** Bila terpaksa menggunakan penomoran manual teks (karena keterbatasan template), format: `[nomor]\t[teks]` dengan tab stop eksplisit pada posisi teks level tersebut. Jangan gunakan spasi sebagai pemisah antara nomor dan teks. Contoh yang benar: `a.\tJudul Temuan` (dengan tab stop di 1080 dxa). Contoh yang salah: `a. Judul Temuan` (spasi biasa, tidak menjamin perataan).

---

### 12.9 Standar Kompatibilitas Google Workspace / Google Docs (GWS) & Tata Letak Tabel
Saat dokumen laporan pengawasan dikonversi, disinkronkan, atau diedit pada Google Docs melalui Google Workspace API / MCP:
1. **Pembersihan Indentasi dalam Sel Tabel (Anti-Loncatan Ruler):**
   - Setiap paragraf di dalam sel tabel wajib dideklarasikan indentasi nol eksplisit: `<w:ind w:left="0" w:right="0" w:firstLine="0"/>` (`indentStart: 0, indentFirstLine: 0`).
   - Paragraf di dalam sel dilarang mewarisi indentasi paragraf global agar penanda biru pada *ruler* Google Docs tidak bergeser ke tengah atau membuat *hanging indent* liar di kolom kedua/ketiga.
2. **Struktur Tabel Metadata & Kop Surat:**
   - **Tabel Nomor/Tanggal Cover (3 Kolom):** Kolom Label (`84 pt`), Kolom Separator `:` (`27.75 pt`), Kolom Nilai (`222.75 pt`). Paragraf sel berindentasi seragam (`14.17 pt`).
   - **Tabel Kop Surat (2 Kolom):** Kolom Logo (`86.7 pt`), Kolom Teks Lembaga (`366.3 pt`). Teks instansi rata tengah murni (`alignment: CENTER`), spasi baris 1.0 tunggal, dan indentasi 0.
   - **Tabel Metadata Surat Pengantar (4 Kolom Terpisah):**
     - Kolom 1 (`69 pt` / `2.43 cm`): Label (`Nomor`, `Lampiran`, `Hal`)
     - Kolom 2 (`18 pt` / `0.63 cm`): Pemisah `:`
     - Kolom 3 (`237.75 pt` / `8.39 cm`): Isi teks nomor/lampiran/judul laporan (*Justified*, indentasi 0)
     - Kolom 4 (`129.75 pt` / `4.58 cm`): Tanggal surat pada baris pertama (*Right-aligned*)
     - *Kaidah Penting:* Tanggal wajib diletakkan pada kolom ke-4 mandiri (bukan *right tab stop* di dalam teks) agar judul laporan pada baris `Hal` tidak mengalami *hanging indent* saat *line wrapping*.
3. **Penyelarasan Narasi di Bawah Sub-Heading Level 1 (`HEADING_3` / `1.`):**
   - Tajuk sub-bagian bernomor (seperti `1. Anggaran Ketahanan Pangan Daerah` pada Informasi Umum) memiliki nomor di `36 pt` dan teks judul di `54 pt`.
   - Paragraf narasi/isi di bawahnya wajib diset persis dengan **`indentStart: 54 pt` (0.75" / 1080 dxa) dan `indentFirstLine: 54 pt`**, sehingga seluruh baris narasi sejajar 100% dengan huruf pertama judul poinnya.


---

### 12.9 Standar Kompatibilitas Google Workspace / Google Docs (GWS) & Tata Letak Tabel
Saat dokumen laporan pengawasan dikonversi, disinkronkan, atau diedit pada Google Docs melalui Google Workspace API / MCP:
1. **Pembersihan Indentasi dalam Sel Tabel (Anti-Loncatan Ruler):**
   - Setiap paragraf di dalam sel tabel wajib dideklarasikan indentasi nol eksplisit: `<w:ind w:left="0" w:right="0" w:firstLine="0"/>` (`indentStart: 0, indentFirstLine: 0`).
   - Paragraf di dalam sel dilarang mewarisi indentasi paragraf global agar penanda biru pada *ruler* Google Docs tidak bergeser ke tengah atau membuat *hanging indent* liar di kolom kedua/ketiga.
2. **Struktur Tabel Metadata & Kop Surat:**
   - **Tabel Nomor/Tanggal Cover (3 Kolom):** Kolom Label (`84 pt`), Kolom Separator `:` (`27.75 pt`), Kolom Nilai (`222.75 pt`). Paragraf sel berindentasi seragam (`14.17 pt`).
   - **Tabel Kop Surat (2 Kolom):** Kolom Logo (`86.7 pt`), Kolom Teks Lembaga (`366.3 pt`). Teks instansi rata tengah murni (`alignment: CENTER`), spasi baris 1.0 tunggal, dan indentasi 0.
   - **Tabel Metadata Surat Pengantar (4 Kolom Terpisah):**
     - Kolom 1 (`69 pt` / `2.43 cm`): Label (`Nomor`, `Lampiran`, `Hal`)
     - Kolom 2 (`18 pt` / `0.63 cm`): Pemisah `:`
     - Kolom 3 (`237.75 pt` / `8.39 cm`): Isi teks nomor/lampiran/judul laporan (*Justified*, indentasi 0)
     - Kolom 4 (`129.75 pt` / `4.58 cm`): Tanggal surat pada baris pertama (*Right-aligned*)
     - *Kaidah Penting:* Tanggal wajib diletakkan pada kolom ke-4 mandiri (bukan *right tab stop* di dalam teks) agar judul laporan pada baris `Hal` tidak mengalami *hanging indent* saat *line wrapping*.
3. **Penyelarasan Narasi di Bawah Sub-Heading Level 1 (`HEADING_3` / `1.`):**
   - Tajuk sub-bagian bernomor (seperti `1. Anggaran Ketahanan Pangan Daerah` pada Informasi Umum) memiliki nomor di `36 pt` dan teks judul di `54 pt`.
   - Paragraf narasi/isi di bawahnya wajib diset persis dengan **`indentStart: 54 pt` (0.75" / 1080 dxa) dan `indentFirstLine: 54 pt`**, sehingga seluruh baris narasi sejajar 100% dengan huruf pertama judul poinnya.


---

## 13. Modul Python Bawaan (Scripts) — Engine Otomatis

Skill ini membundel modul Python siap pakai di folder `scripts/` yang mengimplementasikan seluruh standar formatting di Bagian 12 secara otomatis. **Gunakan modul ini saat membuat dokumen Word (.docx) dari nol** — tidak perlu lagi menulis OOXML manual.

### 13.1 Paket & File

```
scripts/
├── __init__.py
├── bpkp_docx_engine.py    # Engine inti: create_document, numbering, heading, tabel, tanda tangan
└── lhp_builder.py          # Builder tingkat tinggi: BAB I, II, III + temuan 5C
```

### 13.2 Cara Mengimpor

Modul ini dapat diimpor baik dari dalam package maupun sebagai skrip mandiri di workspace penugasan:

```python
# Opsi A — impor langsung (jika sys.path sudah diset)
from bpkp_docx_engine import create_document, add_heading_1, new_bab_context
from lhp_builder import build_bab_i_template, build_bab_iii_temuan

# Opsi B — salin engine ke workspace penugasan lalu impor
sys.path.insert(0, "/path/to/workspace")
from bpkp_docx_engine import create_document
```

### 13.3 API Inti (`bpkp_docx_engine.py`)

| Fungsi | Kegunaan |
|---|---|
| `create_document()` | Buat dokumen kosong dengan A4, margin 3/2/2/2 cm, Arial 12pt, spasi 1.15, heading styles, dan infrastruktur numbering. |
| `new_bab_context(doc, "BAB I")` | Mulai Bab baru → restart semua level numbering ke 1. Kembalikan `num_id`. |
| `new_topic_context(doc, "Topik X")` | Mulai topik baru dalam Bab → nomor topik berlanjut sekuensial. Kembalikan `num_id` Bab. |
| `add_heading_1(doc, text)` | Heading 1 (judul BAB) → muncul di Navigation Panel. |
| `add_heading_2(doc, text, num_id)` | Heading 2 (bagian: A. Simpulan) + numbering level 0. |
| `add_heading_3(doc, text, num_id)` | Heading 3 (topik: 1. Lahan...) + numbering level 1. |
| `add_section_heading(doc, text, num_id, ilvl)` | Heading cetak tebal bernomor (A. / a.) tanpa style Word. |
| `add_topic_heading(doc, text, num_id, ilvl)` | Heading topik (1.) dengan style Heading 3 + numbering. |
| `add_numbered_item(doc, text, num_id, ilvl)` | Paragraf bernomor pada level tertentu. |
| `add_subheading(doc, "a.", text, num_id, ilvl)` | Sub-heading temuan (a. Kondisi). |
| `add_body_sub(doc, text, num_id, ilvl)` | Narasi isi di bawah sub-heading. |
| `add_locus(doc, prefix, name, text, num_id, ilvl)` | Rincian per lokus (1) Provinsi...). |
| `add_detail_item(doc, prefix, text, bold_title, num_id, ilvl)` | Detail item (a) Judul: teks). |
| `add_criteria(doc, text, num_id, ilvl)` | Paragraf Kriteria (merah). |
| `add_cause(doc, text, num_id, ilvl)` | Paragraf Sebab. |
| `add_effect(doc, text, num_id, ilvl)` | Paragraf Akibat. |
| `add_recommendation_block(doc, rec_list, num_id, ilvl)` | Blok rekomendasi (intro + item a) b) c)). |
| `add_signature_block(doc, date, title, name)` | Blok tanda tangan dinas + TTE. |
| `add_table_bordered(doc, rows, cols, col_widths)` | Tabel borderless-BPKP + header shading. Kembalikan (table, rows_data). |
| `add_p(doc, text, ...)` | Paragraf biasa dengan opsi numbering, indent, align. |
| `add_run(p, text, bold, italic, color, size)` | Tambah run ke paragraf dengan font Arial. |

### 13.4 API Builder (`lhp_builder.py`)

| Fungsi | Kegunaan |
|---|---|
| `build_bab_i_template(doc, simpulan_list, rekomendasi_list)` | BAB I: A. Simpulan + B. Rekomendasi. |
| `build_bab_ii_template(doc, latar_belakang, tujuan, ruang_lingkup, dasar_hukum, kelembagaan)` | BAB II: Umum/Pendahuluan. |
| `build_bab_iii_temuan(doc, temuan_list)` | BAB III: Hasil Evaluasi (list temuan 5C). |
| `build_temuan_5c(doc, temuan_dict, num_id)` | Satu temuan 5C: Kondisi, Kriteria, Sebab, Akibat, Rekomendasi. |

### 13.5 Contoh Penggunaan Lengkap

```python
import sys
sys.path.insert(0, r"C:\Users\Admin\.agents\skills\laporan-pengawasan-bpkp\scripts")

from bpkp_docx_engine import create_document, add_p, add_heading_2, add_signature_block
from lhp_builder import build_bab_i_template, build_bab_ii_template, build_bab_iii_temuan

doc = create_document()

# BAB I
build_bab_i_template(
    doc,
    simpulan_list=[
        ("Tata Kelola Lahan Belum Efektif",
         "LP2B belum ditetapkan dengan dasar hukum definitif."),
        ("Program Benih Belum Mandiri",
         "Produksi benih bersertifikat tidak memenuhi kebutuhan."),
    ],
    rekomendasi_list=[
        ("Tata Kelola Lahan",
         ["Menetapkan Perda LP2B.", "Memutakhirkan data LBS."]),
        ("Program Benih",
         ["Mengaktifkan kembali BBU.", "Menyelenggarakan pelatihan penangkar benih."]),
    ],
)

# BAB II
build_bab_ii_template(
    doc,
    latar_belakang="Ketahanan pangan merupakan prioritas nasional...",
    tujuan=["Mengevaluasi tata kelola ketahanan pangan."],
    ruang_lingkup=["Pemerintah Provinsi Papua Tengah."],
    dasar_hukum=["UU Nomor 39 Tahun 2008.", "Perpres Nomor 2 Tahun 2026."],
    kelembagaan="Dinas Tanaman Pangan dan Ketahanan Pangan.",
)

# BAB III (temuan)
build_bab_iii_temuan(doc, temuan_list=[
    {
        "judul": "Tata Kelola Lahan Pertanian",
        "kondisi": "LP2B belum ditetapkan...",
        "kriteria": "(.) Peraturan Menteri Pertanian tentang LP2B.",
        "sebab": "Ketiadaan komitmen Pemda...",
        "akibat": "Lahan pertanian berpindah fungsi...",
        "rekomendasi": ["Menetapkan Perda LP2B.", "Memutakhirkan data LBS."],
    },
])

# Tanda tangan
add_p(doc, "")
add_signature_block(doc, date_text="Nabire, 31 Agustus 2026",
                    title="Kepala Perwakilan,", name="Kriso Wandi Siahaan")

doc.save("LHP.docx")
```

> **Catatan:** Modul ini hanya menyusun **kerangka struktur & format**. Isi/substansi temuan (Kondisi, Kriteria, Sebab, Akibat, Rekomendasi) harus diisi berdasarkan data penugasan aktual. Gunakan prinsip 5C di Bagian 3 dan kualitas komunikasi di Bagian 1 saat mengisi.
