# Skill MPP BPKP (Manajemen Penugasan Pengawasan)

Paket dokumen perencanaan pengawasan dan penyiapan Surat Tugas (ST) otomatis berbasis Peraturan BPKP Nomor 2 Tahun 2023 dan Peraturan BPKP Nomor 4 Tahun 2026 (Tata Naskah Dinas).

## Panduan Lengkap
Silakan baca berkas panduan lengkap:
👉 **[PANDUAN_PENGGUNAAN.md](PANDUAN_PENGGUNAAN.md)**

## Pembaruan Terkini
1. **Sheet `Pegawai` Disembunyikan (Hidden):** Database pegawai disembunyikan di latar belakang; dropdown dan auto-VLOOKUP NIP tetap berfungsi normal.
2. **Pembersihan Total Isian:** Isian tanpa output (Lokasi, Kode Unit, Path Output SIMA-NG, Profil Kop Unit, dan Status Checklist) telah dibersihkan sepenuhnya dari sheet `DATA`.
3. **Panduan & Contoh Isian Langsung di Sheet `DATA`:** Sheet `PANDUAN` dihapus; Kolom D pada sheet `DATA` kini memuat petunjuk dan contoh konkret untuk setiap baris.
4. **Sheet `IHP` 1 Kolom Tunggal:** Butir Insilwas disatukan dalam 1 kolom; skrip otomatis mengekstrak nomor ID dan uraian teksnya.
5. **Seluruh Tim di Sheet `DATA`:** Disediakan slot langsung untuk PM, PT, KT, dan AT 1 s.d. AT 20. Baris tidak terpakai cukup dikosongkan. Isian golongan ditiadakan.
6. **Sheet Libur Dihapus:** Perhitungan hari kerja otomatis mengecualikan Sabtu dan Minggu.

## Ringkasan Cepat

### 1. Menyiapkan Isian
Buka berkas Excel:
`assets/Isian_DATA_MPP_BPKP.xlsx`
(Tersedia hanya 4 sheet aktif: `DATA`, `IHP`, `TEMBUSAN`, dan `JAM_TIM`).

### 2. Menggunakan Prompt AI
Kirimkan prompt ini ke AI Assistant (Antigravity / Codex / Claude):
```text
Gunakan $mpp-bpkp untuk membuat seluruh dokumen MPP dari file isian XLSX ini dalam folder nama penugasannya.
```

### 3. Menggunakan Command Line
- **Inspect**:
  ```powershell
  python scripts/generate_mpp.py "<file.xlsx>" --inspect
  ```
- **Validasi Preflight**:
  ```powershell
  python scripts/generate_mpp.py "<file.xlsx>" --content "<rancangan.json>" --check
  ```
- **Generate Dokumen (DOCX & PDF)**:
  ```powershell
  python scripts/generate_mpp.py "<file.xlsx>" --content "<rancangan.json>" --output-root "D:/autoST/Hasil_MPP"
  ```
