# Berkas Contoh Sintetis MPP BPKP

Folder ini berisi berkas contoh sintetis untuk pengujian fungsi generator dokumen MPP BPKP:

1. **`UJI SINTETIS Evaluasi Nabire.xlsx` & `.json`**:
   - Contoh untuk penugasan non-PIA (Evaluasi).
   - Menghasilkan paket lengkap 12 dokumen (termasuk laporan hasil PIA sebelumnya).
   - Bentuk pengawasan: `EVALUASI` (menggunakan TEO - *Tentative Evaluation Objective*).

2. **`UJI SINTETIS PIA Nabire.xlsx` & `.json`**:
   - Contoh untuk penugasan awal Penelaahan Informasi Awal (PIA).
   - Menghasilkan paket 11 dokumen (laporan hasil PIA belum terbit sehingga ditandai N/A).
   - Bentuk pengawasan: `PIA`.

3. **`KM4_KM5_KM6_acuan_lama.xlsx`**:
   - Berkas acuan format lama untuk perbandingan pemetaan sel DATA.

### Cara Menjalankan Uji Coba:

```powershell
# Dari direktori root mpp-bpkp:
python scripts/generate_mpp.py "examples/UJI SINTETIS Evaluasi Nabire.xlsx" --content "examples/UJI SINTETIS Evaluasi Nabire.json" --cached --check
```
