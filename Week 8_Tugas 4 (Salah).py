from array import array

list_buah = ['apel', 'mangga', 'jeruk']
list_buah.append('anggur')
##list_buah.pop('mangga')
print("list buah :", list_buah)

arr_nilai = array('f', [85.5, 92.0, 78.5, 90.0])
arr_nilai.append(87.0)
nilai_pertama = arr_nilai[0]
##print("nilai pertama adalah: "+ nilai_pertama)
arr_nilai[2] = "delapan puluh"
print("Array nilai: ", arr_nilai)