# Debug Report Diskon Calculator

## Bug 1: Kesalahan Perhitungan Diskon
Penyebab:
Persentase diskon tidak dibagi 100 sehingga nilai diskon menjadi 100 kali lipat.

Solusi:
Menambahkan pembagian 100 pada perhitungan diskon.

## Bug 2: PPN Dihitung Dua Kali
Penyebab:
PPN 10% ditambahkan dua kali ke harga akhir.

Solusi:
Menghapus satu baris penambahan PPN.

## Kesimpulan
Bug berhasil ditemukan menggunakan pdb dan diverifikasi melalui unit testing.
