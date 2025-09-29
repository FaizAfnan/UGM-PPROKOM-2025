print("\nDictionary nilai mahasiswa: ")
nilai_mahasiswa = {
    "Aba": 85,
    "Abi": 90,
    "Abu": 78
}
print(nilai_mahasiswa)

print("\nMenambah nilai Abe: ")
nilai_mahasiswa["Abe"] = 88
print(nilai_mahasiswa)

print("\nMengupdate nilai Abu: ")
nilai_mahasiswa[0] = 87
print(nilai_mahasiswa)

print("\nMencetak semua nilai: ")
for nama, nilai in nilai_mahasiswa:
    print(f"Nilai {nama} adalah {nilai}")
    