"""
Tipe data list
"""
daftar_buku = ['Seven Habits', 'How to Influence People', 'First Things First', '4DX']
print("Tampilkan variabel daftar buku")
print(daftar_buku)

print("\nProses semua dengan for in")
for buku in daftar_buku:
    print(buku)

print("\nTampilkan isi daftar_buku pada indeks tertentu")
print(daftar_buku[0])
print(daftar_buku[2])

print("\nTampilkan dengan for in range")
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

daftar_buku = [1, 'Kenji Volume 2', -313, 3.14]
print("\nTampilkan dengan for in range, dimana tipe data tiap elemen berbeda2")
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nKembalikan nilai awal daftar_buku')
daftar_buku = ['Seven Habits', 'How to Influence People', 'First Things First', '4DX']
print('\nTambahkan 1 buku baru')
daftar_buku.append('Dunia Matematika Kelas 5')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print("\nClear list")
daftar_buku.clear()
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print("\nGanti elemen pertama")
daftar_buku = ['Seven Habits', 'How to Influence People', 'First Things First', '4DX']
daftar_buku[0] = 'Eight Habits'
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print("\nAmbil elemen ke-2")
buku = daftar_buku.pop(1)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print("\nBuku yang diambil tadi")
print(buku)

print("\nPop")
daftar_buku.pop()
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print("\nPop minus")
daftar_buku = ['Seven Habits', 'How to Influence People', 'First Things First', '4DX']
daftar_buku.pop(-1)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])
# Pop sering digunakan untuk tipe data stack

print("\nPerintah del")
daftar_buku = ['Seven Habits', 'How to Influence People', 'First Things First', '4DX']
del daftar_buku[0]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print("\nPerintah del dengan list comprehension")
daftar_buku = ['Seven Habits', 'How to Influence People', 'First Things First', '4DX']
del daftar_buku[:]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print("\nPerintah del dengan list comprehension [start:stop]")
daftar_buku = ['Seven Habits', 'How to Influence People', 'First Things First', '4DX']
del daftar_buku[0:3]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print("\nPerintah del dengan list comprehension [start:stop]")
daftar_buku = ['Seven Habits', 'How to Influence People', 'First Things First', '4DX']
del daftar_buku[0:-2]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print("\nPerintah del dengan list comprehension [start:stop:step]")
daftar_buku = ['Seven Habits', 'How to Influence People', 'First Things First', '4DX']
del daftar_buku[0::2]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])
