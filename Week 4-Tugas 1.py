#program persyaratan SIM
umur = int(input("masukkan umur anda: "))
nilai = int(input("masukkan nilai tes anda: "))
lulus = "selamat anda berhak mendapatkan SIM anda"
gagal = "Maaf anda tidak berhak mendapatkan SIM anda\nSilahkan coba lagi bulan atau tahun depan"
if (umur > 17):
    if (nilai < 60):
        print()
        print(gagal)
    else:
        print(lulus)
else:
    print()
    print(gagal)