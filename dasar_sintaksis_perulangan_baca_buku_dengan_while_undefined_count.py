"""
Program perulangan membaca buku dengan while sampai paham
"""

buku = 10
print('Ibu berkata, "Baca semua bukumu"')
jumlah_baca = 0

jumlah_paham = 0
print(f'jumlah buku yang sudah dibaca dan dipahami {jumlah_paham}')

while jumlah_baca < buku * 2:
     jumlah_baca = jumlah_baca + 1
     if jumlah_paham == 9:
         print(f"Buku ke {jumlah_paham + 1} belum paham")
     else:
         jumlah_paham = jumlah_paham + 1
         print(f"Buku ke {jumlah_paham} Sudah dibaca dan dipahami")
print(f'Jumlah buku yang sudah dibaca dan dipahami {jumlah_paham}')
if jumlah_paham == buku:
    print('"Bu, Semua buku sudah dibaca dan dipahami"')
else:
    print(f'"Bu, Tidak semua buku bisa dipahami'
          f'Budi hanya bisa memahami {jumlah_paham} buku')
