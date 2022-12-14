"""
Semua sintaksis dasar bahasa pemprograman terdiri dari:
1. Sekuensial: langkah berurutan
2. Percabangan: langkah melompat jika kondisi terpenuhi
3. Perulangan: mengulang langkah berkali-kali selama/sampai kondisi terpenuhi
"""

# Sekuensial
print('Ibu berkata, "Pergi ke toko"')
print('Budi menjawab, "Baik, apa yang harus saya lakukan di toko?"')
print('Ibu menjawab, "Beli satu botol susu, dan jika ada telur beli 6"')
print("Maka budi berangkat ke toko")
print("Dan mulai berbelanja")

# Percabangan
jumlah_botol_susu = 1

if jumlah_botol_susu > 0:
    print("Budi mengecek harganya, dan ternyata uangnya cukup")
    print("Budi membeli 1 botol susu")
else:
    print("Budi tidak jadi membeli 1 botol susu")

print("Budi pulang ke rumah")
print("Menyerahkan hasilnya kepada ibu")

# Percabangan tingkat lanjut
jumlah_susu = 173
jumlah_butir_telur = 1587
print(f"jumlah botol susu {jumlah_susu} botol")
print(f"jumlah telur {jumlah_butir_telur} butir")

if jumlah_susu > 0:
    print("Budi mengecek harganya, dan ternyata uangnya cukup")
    if jumlah_butir_telur == 0:
        print("Budi membeli 1 botol susu")
    else:
        print("Budi membeli 6 botol susu")
else:
    print("Budi tidak jadi membeli 1 botol susu")

print("Budi pulang ke rumah")
print("Menyerahkan hasilnya kepada ibu")


