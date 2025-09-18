jumlah = int(input("Masukkan jumlah nilai yang ingin dihitung rata ratanya: "))
total = 0  
for i in range(1, 1 + jumlah):
    nilai = float(input(f"Masukkan nilai ke-{i}: "))
    total += nilai  
rata_rata = total / jumlah
print(f"Rata-rata dari {jumlah} nilai adalah: {rata_rata}")