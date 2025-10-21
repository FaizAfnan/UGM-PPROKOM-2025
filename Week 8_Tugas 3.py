from array import array
data_array = array ('i', [])
for i in range(5):
    input_data_array = int(input(f"Masukkan elemen array ke-{i+1}: "))
    data_array.append(input_data_array)
for i, j in enumerate(data_array):
    print(f"Elemen array ke-{i+1}: {j}")
len_array = len(data_array)
print(f"jumlah elemen dalam array : {len_array} elemen")
jumlah_total = sum(data_array)
print(f"jumlah total elemen dalam array : {jumlah_total}")
rata_rata = jumlah_total / len_array
print(f"rata-rata elemen dalam array : {rata_rata}")