"""
List
1. Struktur data
2. Mengatur dan menyimpan data dengan python
"""
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(states_of_america[-1])

states_of_america[1] = "pencilvania"
print(states_of_america)

daftar_buku = ["Seven Habits", "How to Influence People", "First Things First"]
print("Tampilkan variable daftar buku")
print(daftar_buku)

print("\nProses semua dengan for in")
for buku in daftar_buku:
    print(buku)

print("\nTampilkan isi daftar buku pada indeks tertentu")
print(daftar_buku[0])
print(daftar_buku[2])

print("\nTampilkan dengan for in range")
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

daftar_buku = [1, "Kenji Volume 2", -313, 3.14]
print("\nTampilkan dengan for in range, dimana tipe data tiap elemen berbeda2")
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print("\nKembalikan nilai awal daftar buku")
daftar_buku = ["Seven Habits", "How to Influence People", "First Things First"]
print("\nTambahkan 1 buku baru")
daftar_buku.append("Dunia matematika kelas 5")
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])
