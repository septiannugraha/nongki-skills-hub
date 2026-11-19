# Format tabel dan status rujukan

## Keputusan format

Tata Naskah Dinas BPKP tidak boleh diringkas sebagai kewajiban semua tabel tanpa garis kiri, kanan, dan antarkolom. Gunakan format sesuai jenis naskah serta aturan/formulir khusus yang berlaku. Mempertahankan garis berkotak pada templat yang memerlukannya dan memilih tabel terbuka untuk narasi adalah dua pilihan yang berbeda konteks.

| Konteks | Perlakuan |
|---|---|
| Formulir dengan contoh/templat khusus | Pertahankan garis luar, antarkolom, dan pemisah baris sesuai format; jangan menghapusnya secara massal |
| Formulir KM 4/KM 5/KM 6 | Ikuti instrumen kendali mutu unit/aplikasi, termasuk kolom, satuan waktu, dan border |
| Pakta integritas dengan templat berkotak | Tabel identitas dan tanda tangan memakai garis luar lengkap serta pemisah kolom/baris; pertahankan bentuk berkotak tersebut |
| Kop, metadata, atau blok tanda tangan yang memakai tabel tata letak | Gunakan garis tercetak sesuai contoh; border dapat kosong tanpa mengubah aturan tabel data |
| Tabel data naratif tanpa format khusus | Pilih garis berkotak atau gaya horizontal saja menurut kebutuhan keterbacaan/permintaan; nyatakan statusnya sebagai pilihan desain |

Tidak adanya ketentuan umum border tidak berarti seluruh tabel harus diberi semua garis. Tujuannya adalah mempertahankan bentuk yang relevan bagi dokumen tersebut.

## Dasar dan lokasi sumber

Sumber: [Peraturan BPKP Nomor 4 Tahun 2026](https://peraturan.bpk.go.id/Details/359710/peraturan-bpkp-no-4-tahun-2026-tata-naskah-dinas-di-lingkungan-badan-pengawasan). Rujukan berikut mengikuti penomoran halaman peraturan.

- **BAB V-C, angka 20, Formulir**, akhir pembahasan sebelum halaman bernomor 159: format/desain mengikuti kebutuhan informasi, kegunaan, isi, penampilan fisik, atau ketentuan perundang-undangan. Contoh routing slip terdapat pada **Gambar V.52, halaman bernomor 159**.
- **BAB V-C.14, Surat Pernyataan**, halaman 149–150: mengatur kepala, batang tubuh, kaki, dan contoh surat pernyataan umum (Gambar V.47). Jangan mengubahnya menjadi klaim kewajiban border tabel pakta yang tidak disebut secara khusus. Bingkai besar di sekitar contoh adalah penyajian ilustrasi naskah; bedakan dari border tabel di dalam naskah.
- **BAB V-A, angka 1 huruf d**, halaman bernomor 73: SOP mengikuti pedoman penyusunan SOP tersendiri. Jangan menyimpulkan rincian SOP hanya dari ketentuan TND umum.
- **BAB II-D.1–2**, halaman bernomor 22–23: jarak antarunsur, penyesuaian jarak baris, Arial 11/12, dan pengecualian Bookman Old Style 12 untuk produk hukum.
- **BAB II-E**, halaman bernomor 23–24: ruang tepi atas/bawah/kiri/kanan dan kelonggaran penyesuaian.

Pustaka Word yang tersedia dalam skill memberikan bukti implementasi format yang berbeda:

- `../assets/templates/Routing_Slip.docx`: tabel kendali memiliki border sel kiri dan kanan `single`.
- `../assets/templates/SOP.docx`: tabel memuat border luar `single`, `insideH`, dan `insideV`.

Bukti XML templat menjelaskan apa yang tercetak pada berkas itu; bukti tersebut tidak menetapkan bahwa seluruh tabel harus menggunakan gaya yang sama. Bila keaslian atau versi templat belum jelas, cocokkan lagi dengan peraturan/format khusus sumbernya.

Bila templat pakta memakai tabel identitas dan tanda tangan berkotak, pertahankan garis luar dan pemisah baris serta kolom. Sesuaikan jumlah halaman dengan jumlah personel.

## Pemeriksaan Word/Excel

1. Tentukan apakah tabel merupakan tabel data, formulir, atau alat tata letak.
2. Bandingkan dengan contoh visual yang relevan; ekstraksi Markdown tidak menyimpan garis tabel dan dapat melewatkan gambar.
3. Pada Word, periksa `w:tblBorders`, `w:tcBorders`, dan border dari style. Border sel dapat menimpa border tingkat tabel.
4. Pada Excel, bedakan gridlines editor dari border sel yang ikut tercetak. Periksa pengaturan cetak dan pratinjau PDF.
5. Pertahankan struktur saat mengganti isi. Header shading abu-abu, font tabel 10 pt, padding sel tertentu, dan gaya horizontal saja merupakan pilihan implementasi kecuali ada sumber khusus yang menetapkannya.

## Batas penggunaan resep teknis

Resep generator membantu membuat dokumen konsisten, tetapi tidak menjadi dasar normatif baru. Jika resep teknis bertentangan dengan jenis naskah atau formulir yang berlaku, sesuaikan resep tersebut. Kertas, font, ruang tepi, spasi, struktur, penomoran, kop, dan kewenangan tanda tangan harus ditelusuri ke ketentuan masing-masing, bukan diturunkan dari satu contoh laporan.
