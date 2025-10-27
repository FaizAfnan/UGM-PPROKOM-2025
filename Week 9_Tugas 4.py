nilai = [
[85, 80, 90],
[78, 82, 88],
[92, 90, 94],
[70, 68, 72],
[88, 85, 84],
[60, 75, 70],
[95, 92, 98],
[74, 70, 76],
[81, 85, 83],
[69, 72, 70],
[90, 88, 92],
[76, 80, 79],
[84, 86, 90],
[79, 82, 85],
[67, 70, 68],
[91, 94, 93],
[73, 78, 75],
[87, 84, 89],
[65, 68, 70],
[93, 90, 95],
[77, 80, 78],
[82, 84, 88],
[89, 85, 90],
[71, 74, 76]
]
for i, (tugas, uts, uas) in enumerate(nilai):
    print (f"Nilai mahasiswa ke-{i+1} : Tugas={tugas}, UTS={uts}, UAS={uas}")

import numpy as np
print()
print("Rata-rata nilai mahasiswa: ", np.mean(nilai))
print("Rata-rata nilai Tugas mahasiswa: ", np.mean([tugas for tugas, uts, uas  in nilai]))
print("Rata-rata nilai UTS mahasiswa: ", np.mean([uts for tugas, uts, uas  in nilai]))
print("Rata-rata nilai UAS mahasiswa: ", np.mean([uas for tugas, uts, uas  in nilai]))
print("Nilai tertinggi mahasiswa: ", np.max(nilai))
print("Nilai Terendah mahasiswa: ", np.min(nilai))
print("Nilai tertinggi Tugas: ", np.max([tugas for tugas, uts, uas  in nilai]))
print("Nilai Terendah Tugas: ", np.min([tugas for tugas, uts, uas  in nilai]))
print("Nilai tertinggi UTS: ", np.max([uts for tugas, uts, uas  in nilai]))
print("Nilai Terendah UTS: ", np.min([uts for tugas, uts, uas  in nilai]))
print("Nilai tertinggi UAS: ", np.max([uas for tugas, uts, uas  in nilai]))
print("Nilai Terendah UAS: ", np.min([uas for tugas, uts, uas  in nilai]))
