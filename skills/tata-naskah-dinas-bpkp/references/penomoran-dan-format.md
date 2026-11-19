# Penomoran dan Format Naskah Dinas BPKP

Referensi format penomoran, kode jenis naskah, kop, kertas, spasi, dan ruang tepi sesuai **BAB II Pembuatan Naskah Dinas**, serta desain formulir menurut **BAB V-C.20**, Peraturan BPKP Nomor 4 Tahun 2026. Pilihan implementasi Word dibedakan dari ketentuan peraturan.

---

## 1. Format Penomoran Naskah Dinas

Nomor naskah dinas adalah segmen penting kearsipan; susunannya harus memudahkan penyimpanan, penemuan kembali, dan penilaian arsip. Setiap unit kerja wajib menggunakan penomoran sesuai ketentuan.

Peraturan 4/2026 membagi penomoran menjadi **dua format**:

### Format 1: Tanpa Kode Jenis (Naskah Dinas Arahan Pengaturan)
Digunakan untuk Peraturan, Instruksi, dan Surat Edaran. Hanya menyebutkan nomor dan tahun penetapan, tanpa kode jenis, penanda tangan, dan unit kerja konseptor.
```
(Nama Jenis Naskah Dinas)
(Nama Jabatan)
NOMOR xxx TAHUN xxxx
TENTANG
(Judul Hal yang Diatur)
```

### Format 2: Dengan Kode Jenis (Umum)
Untuk naskah dinas selain Peraturan/Instruksi/Surat Edaran:
```
[kode klasifikasi arsip] / [kode keamanan] / [kode jenis] - [nomor urut] / [kode unit penanda tangan] / [kode konseptor] / [tahun]
```

Contoh riil naskah pengawasan BPKP di lapangan:
1. **Surat Tugas (ST):** `PE.09.02/ST-314/PW36/2/2026`
   - `PE.09.02`: Kode klasifikasi pengawasan bidang pangan/IPP
   - `ST-314`: Jenis Surat Tugas dengan nomor urut 314
   - `PW36`: Kode Kantor Perwakilan BPKP Provinsi Papua Tengah
   - `2`: Kode Bidang (IPP / Akuntabilitas Pemerintah Daerah)
   - `2026`: Tahun anggaran pelaksanaan tugas
2. **Laporan Hasil Pengawasan / Evaluasi (LHP):** `PE.09.03/LHP-314/PW36/2/2026`
3. **Nota Dinas Internal Kantor Pusat:** `HO-01.02/ND-001/SU 01 1/2026`

### Pola nomor pada templat

Templat Surat Dinas, Surat Dinas Kepala/Wakil Kepala, dan Surat Pengantar Penugasan memakai pola `[kode klasifikasi arsip]/[kode keamanan]/S-[nomor urut]/[kode unit]/[tahun]` tanpa kode konseptor. Contoh surat Rahasia `PW.01.03/R/S-7/PW16/2026` dan surat Biasa `PW.01.03/S-7/PW16/2026`.

Surat dinas penyampaian Notisi memakai nomor surat dinas. Notisi pertama yang disampaikan langsung oleh tim dan Notisi yang dilampirkan pada surat dinas mengikuti format Notisi pada BAB V-C.1.

`generate_naskah.py` membaca pola nomor pada templat. Untuk nomor yang telah ditetapkan, gunakan `nomor_lengkap`.

### Kode Keamanan (Khusus Surat Dinas)
- `SR` : Sangat Rahasia
- `R`  : Rahasia
- `T`  : Terbatas
- Biasa tanpa kode di nomor surat. Kode `B` dipakai dalam pengendalian naskah masuk.

### Pengecualian Penomoran
- **Tanpa kode jenis**: Peraturan, Instruksi, Surat Edaran (Format 1).
- **Tidak dibubuhi penomoran sama sekali**: Disposisi, Dokumentasi Pengawasan, Pedoman, Panduan Teknis Pengawasan, Petunjuk Pelaksanaan/Teknis, Telaah Staf, Kerangka Acuan Kerja, dan Formulir. Tata cara penomorannya tidak mengikuti format di Peraturan Badan ini; mengikuti kebijakan unit kerja.

### Aturan Nomor Urut
Nomor urut adalah nomor agenda elektronik unit kerja dalam 1 (satu) tahun takwim/kalender, menggunakan angka arab berurutan. Setiap awal tahun, per kelompok buku agenda elektronik, dimulai dari nomor urut 1. Pengelompokan per jenis Naskah Dinas (tidak digabung). **DILARANG** menambahkan kode, huruf, angka romawi, atau penanda lain yang mengubah format.

### Kode Konseptor
Kode unit/jabatan/konseptor menunjukkan siapa pejabat yang menandatangani Naskah Dinas dan unit kerja konseptor asal. Dipisahkan dengan garis miring (`/`) antara kode penanda tangan dan konseptor. Pencantuman kode konseptor hanya sampai satu tingkat di bawah pejabat penanda tangan. Daftar kode ditetapkan oleh Kepala (melalui petunjuk teknis terpisah).

### Kode Perwakilan & Akronim Unit Kerja
Peraturan 4/2026 menambahkan penggunaan **kode konseptor, kode perwakilan, dan akronim unit kerja** di lingkungan BPKP. Petunjuk teknisnya ditetapkan oleh Kepala.

---

## 2. Kode Jenis Naskah Dinas (Peraturan BPKP 4/2026)

### a. Naskah Dinas Arahan
| Naskah | Kode |
|---|---|
| Peraturan | Tanpa kode (Format 1) |
| Instruksi | Tanpa kode (Format 1) |
| Surat Edaran | Tanpa kode (Format 1) |
| Standar Operasional Prosedur (SOP) | Tanpa kode |
| Keputusan | `KEP` |
| Surat Perintah | `SPRIN` |
| Surat Tugas | `ST` |

### b. Naskah Dinas Korespondensi
| Naskah | Kode |
|---|---|
| Nota Dinas | `ND` |
| Memorandum | `MO` |
| Disposisi | Tanpa kode, tanpa nomor |
| Undangan Internal | `UND` |
| Surat Dinas | `S` |

### c. Naskah Dinas Khusus
| Naskah | Kode |
|---|---|
| Dokumentasi Pengawasan | Tanpa kode, tanpa nomor |
| Pedoman | Tanpa kode, tanpa nomor |
| Panduan Teknis Pengawasan | Tanpa kode, tanpa nomor |
| Petunjuk Pelaksanaan/Teknis | Tanpa kode |
| Laporan Hasil Pengawasan | `LHP` |
| Laporan Penunjang Pengawasan | `LPP` |
| Nota Kesepahaman/MoU | `MoU` |
| Surat Perjanjian | `PRJ` |
| Berita Acara | `BA` |
| Surat Kuasa | `KS` |
| Surat Keterangan | `KET` |
| Surat Pengantar Naskah/Barang | `SP` |
| Pengumuman | `PENG` |
| Surat Peringatan | `PRT` |
| Surat Pernyataan | `SPT` |
| Notula/Risalah | `NOTULA` |
| Telaah Staf | Tanpa kode, tanpa nomor |
| Sertifikat | `SERT` |
| Piagam Penghargaan | `PI` |
| Kerangka Acuan Kerja | Tanpa kode, tanpa nomor |
| Formulir | Tanpa kode, tanpa nomor |

> [!note] Perubahan Kode Jenis (Perban 4/2022 → Peraturan 4/2026)
> - **Dihapus**: `SPD` (Surat Perjalanan Dinas -- kini peraturan terpisah), `SPPL` (Surat Pengukuhan Perintah Lisan), `BAPS` (BA Pengangkatan Sumpah), `NST` (Naskah Serah Terima Jabatan), `SI` (Surat Izin), `SPMT`/`SPMJ`/`SPL` (diganti `SPT`).
> - **Kode berubah**: Surat Kuasa dari tanpa kode → `KS`; Surat Pernyataan dari gabungan `SPMT`/`SPMJ`/`SPL` → `SPT`; Memorandum kini eksplisit `MO`.
> - **Kode baru**: `NOTULA`, `SERT`, `PI`.

---

## 3. Buku Agenda & Penomoran Awal Tahun

Pencatatan naskah dalam buku agenda elektronik dikelompokkan per jenis Naskah Dinas (tidak digabung beberapa jenis). Setiap awal tahun kalender, penomoran pada seluruh buku agenda dimulai kembali dari nomor urut 1.

---

## 4. Kop Naskah Dinas Resmi (Unit Pusat & Perwakilan)

Kop surat naskah dinas resmi memuat lambang negara/logo BPKP dan identitas unit kerja:
- **Struktur Kop 2 Kolom:**
  - **Kolom Kiri (Lebar ~2,5 cm):** Logo BPKP berwarna proporsional (panjang 3,4 cm, tinggi 1,7 cm).
  - **Kolom Kanan (Lebar ~13,5–14 cm):** Teks lembaga resmi:
    - Baris 1: `BADAN PENGAWASAN KEUANGAN DAN PEMBANGUNAN` (Arial 11 pt Bold)
    - Baris 2: `PERWAKILAN PROVINSI [NAMA PROVINSI]` (Arial 12 pt Bold)
    - Baris 3: `Jalan [Alamat Lengkap Kantor, Kode Pos]` (Arial 9 pt Regular)
    - Baris 4: `Telepon: [...], Faksimile: [...], Email: [...]@bpkp.go.id, Website: www.bpkp.go.id` (Arial 9 pt Regular)
- **Garis Pemisah Kop:** Garis horizontal solid hitam memanjang selebar margin naskah.

---

## 5. Standar Format Dokumen Microsoft Word (`docx`)

### A. Ukuran Kertas & Margin
- **Kertas:** A4 (21,0 cm x 29,7 cm)
- **Ruang Tepi (BAB II-E):** Atas 10 mm bila memakai kop, paling kurang 20 mm tanpa kop/pada halaman berikutnya; bawah paling kurang 25 mm; kiri paling kurang 30 mm untuk media kertas atau 20 mm untuk elektronik; kanan paling kurang 20 mm. Pengaturan fleksibel dengan mempertimbangkan isi, keserasian, dan estetika.

### B. Tipografi & Spasi
- **Font Umum (BAB II-D.2):** **Arial 11 atau 12 pt**; produk hukum berupa peraturan, instruksi, surat edaran, dan keputusan menggunakan **Bookman Old Style 12 pt**. Ikuti ukuran khusus kop/judul sesuai jenis naskah.
- **Spasi (BAB II-D.1):** Ikuti jarak antarunsur dan sesuaikan jarak baris dengan keperluan/estetika. Spasi 1,15 dan space after 6 pt adalah pilihan implementasi narasi, bukan kewajiban universal.
- **Perataan:** Sesuaikan format judul, metadata, narasi, angka, dan tabel; jangan memaksa semua unsur rata kiri-kanan.

### C. Hierarki Indentasi & Tab Stops (Anti-Bocor / Hanging Indent)
- **Level 1 (Topik/Bab):** Left `0.00"`, First Line `0.00"`, Bold 12 pt.
- **Level 2 (Sub-Heading `a.`, `b.`):** Left `0.75"` (1080 dxa), First Line `-0.25"` (-360 dxa), Tab Stop di `1440 dxa` (`1.00"`), Bold 12 pt.
- **Level 2 Body (Narasi Pengantar):** Left `1.00"` (1440 dxa), First Line `0.00"`, Regular 12 pt, Justified.
- **Level 3 (Rincian Lokus `1)`, `2)`):** Left `1.25"` (1800 dxa), First Line `-0.25"` (-360 dxa), Tab Stop di `1800 dxa` (`1.25"`), Justified, Nama Lokus Regular.
- **Level 4 (Detail Item `a)`, `b)`):** Left `1.50"` (2160 dxa), First Line `-0.25"` (-360 dxa), Tab Stop di `2160 dxa` (`1.50"`), Justified.

### D. Format Tabel Sesuai Jenis Naskah/Formulir
- Tidak ada dasar untuk menerapkan larangan border kiri/kanan/vertikal pada semua tabel. Pertahankan border contoh/templat yang berlaku. BAB V-C.20 membolehkan desain formulir sesuai kebutuhan informasi, kegunaan, isi, penampilan, atau ketentuan khusus.
- Tabel kendali pada `assets/templates/Routing_Slip.docx` memiliki border kiri/kanan; tabel `assets/templates/SOP.docx` memiliki border luar dan antarkolom. Jangan menghapusnya demi menyeragamkan gaya.
- Bedakan tabel data/formulir dari tabel tata letak metadata, kop, atau blok tanda tangan yang dapat tanpa garis tercetak.
- Gaya garis horizontal saja (*open table*), header `#F2F2F2`, dan padding 100/150 dxa dapat dipilih untuk tabel naratif yang tidak memiliki format khusus. Itu pilihan desain, bukan kewajiban umum TND.
- Periksa border pada tingkat tabel, sel, dan style, lalu pratinjau hasil cetak. Rujukan serta langkah keputusan lengkap: [Format Tabel dan Status Rujukan](format-tabel-dan-rujukan.md).

### E. Format Khusus Google Workspace / Google Docs (GWS)
- **Tabel Metadata Surat Pengantar:** Wajib menggunakan format **4 Kolom** (Kolom 1: Label `69 pt`, Kolom 2: `:` `18 pt`, Kolom 3: Konten/Judul `237.75 pt`, Kolom 4: Tanggal Kanan `129.75 pt`) untuk mencegah *hanging indent* pada *line wrapping* judul `Hal`.
- **Indeks Kolom Tabel:** Setiap paragraf di dalam sel tabel wajib dideklarasikan `<w:ind w:left="0" w:right="0" w:firstLine="0"/>` (`indentStart: 0, indentFirstLine: 0`) agar *marker ruler* Google Docs tidak bergeser ke tengah.
- **Narasi Sub-Heading Level 1 (`HEADING_3`):** Paragraf narasi diset dengan `indentStart: 54 pt` (0.75" / 1080 dxa) dan `indentFirstLine: 54 pt` agar sejajar 100% dengan huruf pertama judul sub-heading.

### F. Resep Lengkap Numbering Multi-Level untuk Google Docs (XML)

Untuk daftar bertingkat `A. → 1. → a.` yang merender benar di Google Docs, bangun `word/numbering.xml` dengan definisi `abstractNum` berikut (terverifikasi):

```xml
<abstractNum abstractNumId="1">
  <lvl ilvl="0"> <numFmt w:val="upperLetter"/> <lvlText w:val="%1."/> <lvlJc w:val="left"/> <pPr><ind w:left="720"  w:hanging="360"/></pPr> </lvl>
  <lvl ilvl="1"> <numFmt w:val="decimal"/>     <lvlRestart w:val="1"/> <lvlText w:val="%2."/> <lvlJc w:val="left"/> <pPr><ind w:left="1080" w:hanging="360"/></pPr> </lvl>
  <lvl ilvl="2"> <numFmt w:val="lowerLetter"/> <lvlRestart w:val="2"/> <lvlText w:val="%3."/> <lvlJc w:val="left"/> <pPr><ind w:left="1440" w:hanging="360"/></pPr> </lvl>
  <lvl ilvl="3"> <numFmt w:val="decimal"/>     <lvlRestart w:val="3"/> <lvlText w:val="%4)"/> <lvlJc w:val="left"/> <pPr><ind w:left="1800" w:hanging="360"/></pPr> </lvl>
  <lvl ilvl="4"> <numFmt w:val="lowerLetter"/> <lvlRestart w:val="4"/> <lvlText w:val="%5)"/> <lvlJc w:val="left"/> <pPr><ind w:left="2160" w:hanging="360"/></pPr> </lvl>
</abstractNum>
<num numId="1"><abstractNumId w:val="1"/></num>
```

Pemakaian pada paragraf: `<w:numPr><w:ilvl w:val="N"/><w:numId w:val="1"/></w:numPr>` dengan `w:ind` identik nilai `left` dan `hanging` pada level terkait.

**Teknik tercekat (metode salin-referensi):** membangun `numbering.xml`/`styles.xml` dari nol berulang kali gagal render di Google Docs. Metode yang selalu berhasil: **salin docx referensi berformat benar → kosongkan seluruh paragraf dan tabelnya (`p._p.getparent().remove(p._p)`) → tulis ulang konten**. Numbering, styles, dan section properties terwarisi utuh.

**Peringatan nilai piksel vs dxa:** jangan gunakan konversi piksel (708/1068/1428). Nilai baku wajib kelipatan grid 360 dxa: `720/1080/1440`. Selisih 12 dxa tidak kasat mata tetapi membuat *marker ruler* Google Docs tidak jatuh pada grid 0,5"/0,75"/1,0".

**Penyelarasan tabel dengan teks:** agar garis tepi kiri tabel rata sejajar teks narasi di atasnya (bukan menonjol keluar), setel `w:tblPr` dengan `<w:jc w:val="left"/>`, `<w:tblInd w:w="720" w:type="dxa"/>` (identik `w:ind w:left` paragraf), dan `<w:tblW w:w="8318" w:type="dxa"/>` (lebar efektif = lebar halaman minus kedua margin minus indent). Isi `w:tcW` tiap sel dengan jumlah yang sama persis.

