stok_buku = {
    "Harry Potter": 10,
    "Laskar Pelangi": 15,
    "Bumi Manusia": 7,
    "Dilan 1990": 20
}
print("\nBuku yang tersedia dan stoknya: ")
for judul, stok in stok_buku.items():
    print(f"{judul}: {stok} buku")

Judul_buku_baru = input("\nMasukkan judul buku baru: ")
stok_buku_baru = int(input("Masukkan stok buku baru: "))
stok_buku[Judul_buku_baru] = stok_buku_baru
print(f"\nBuku {Judul_buku_baru} berhasil ditambahkan dengan stok {stok_buku_baru}")
print("\nBuku yang tersedia setelah ditambah buku baru:")
for judul, stok in stok_buku.items():
    print(f"{judul}: {stok} buku")