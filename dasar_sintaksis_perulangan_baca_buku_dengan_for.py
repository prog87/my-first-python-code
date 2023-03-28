"""
Program perulangan membaca buku dengan perintah for
1. perintah for jelas berapa perulangannya
2. Tidak jelas berapa kali akan diulang tetapi jelas kapan selesainya
"""
jumlah_buku = 100
print('Ibu berkata, "Baca semua bukumu"')

jumlah_buku_yang_sudah_dibaca = 0
print(f"Jumlah buku yang sudah dibaca {jumlah_buku_yang_sudah_dibaca}")

# angka pada coding dimulai dari 0
# range(1, 11) dibaca 11-1 = 10
# perintah for hanya bisa mengulang sejumlah yang dipastikan 1-10
print("Dengan for")
for jumlah_buku_yang_sudah_dibaca in range(1, jumlah_buku+1):
    print(f"Buku ke {jumlah_buku_yang_sudah_dibaca} sudah dibaca")

print(f"Jumlah buku yang sudah dibaca {jumlah_buku_yang_sudah_dibaca}")

# tanpa for
print("Membaca buku ke-1")
print("Membaca buku ke-2")
print("Membaca buku ke-3")
print("Membaca buku ke-4")
print("Membaca buku ke-5")
print("Membaca buku ke-6")
print("Membaca buku ke-7")
print("Membaca buku ke-8")
print("Membaca buku ke-9")
print("Membaca buku ke-10")
