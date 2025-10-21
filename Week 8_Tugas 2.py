nama = []
for i in range(5):
    nama_input = input(f"Masukkan nama teman ke-{i+1}:")
    nama.append(nama_input)
print("Daftar nama teman: ", nama)
for i, j in enumerate(nama):
    print(f"Teman ke-{i+1} adalah {j}")
print("ingin mengganti nama teman pada indeks ke berapa?")
ganti_nama = int(input("Masukkan indeks nama yang ingin diganti (0-4): "))
if 0 <= ganti_nama < len(nama):
    nama_baru = input("Masukkan nama baru: ")
    nama[ganti_nama] = nama_baru
    print("daftar nama teman setelah diperbarui:")
    for i, j in enumerate(nama):
        print(f"Teman ke-{i+1} adalah {j}")
else: 
    print("Indeks tidak valid.") 

