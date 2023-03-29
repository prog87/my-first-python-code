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

print("\nmembuat list comprehension baru")
daftar_buku = ['Seven Habits', 'How to Influence People', 'First Things First', '4DX']
daftar_buku_baru = daftar_buku[:]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print("\nmembuat list comprehension: ganjil")
daftar_buku = ['1 Seven Habits', '2 How to Influence People', '3 First Things First', '4 4DX']
daftar_buku_baru = daftar_buku[0::2]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print("\nmembuat list comprehension: genap")
daftar_buku = ['1 Seven Habits', '2 How to Influence People', '3 First Things First', '4 4DX']
daftar_buku_baru = daftar_buku[1::2] #start:stop:end
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print("\nmembuat list comprehension: minus")
daftar_buku = ['1 Seven Habits', '2 How to Influence People', '3 First Things First', '4 4DX']
daftar_buku_baru = daftar_buku[0:-1]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print("\nmembuat list comprehension: ganjil")
daftar_buku = ['1 Seven Habits', '2 How to Influence People', '3 First Things First', '4 4DX']
print(daftar_buku[0::2]) #menyederhanakan perintah print

