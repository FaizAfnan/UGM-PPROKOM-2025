nama = []
nim = []

def tambah_data(nama_mhs, nim_mhs):
    nama.append(nama_mhs)
    nim.append(nim_mhs)
def tampil_data():
    for i in range(len(nama)):
        print(f"{i+1}. {nama[i]} ({nim[i]})")