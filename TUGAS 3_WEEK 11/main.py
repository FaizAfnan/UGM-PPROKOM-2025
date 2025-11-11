import data_mhs as dm

while True:
    print("\n==Menu Data Mahasiswa==")
    print("1. Tambah Data")
    print("2. Tampilkan Data")
    print("3. Keluar")
    
    pilihan = input("Pilih menu (1-3): ")
    
    if pilihan == '1':
        nama_mhs = str(input("Masukkan Nama Mahasiswa: "))
        nim_mhs = input("Masukkan NIM Mahasiswa: ")
        dm.tambah_data(nama_mhs, nim_mhs)
        print (f"Data mahasiswa {nama_mhs} ({nim_mhs}) berhasil ditambahkan.")
    elif pilihan == '2':
        print("\n== Daftar Mahasiswa ==")
        dm.tampil_data()
    elif pilihan == '3':
        print("Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")