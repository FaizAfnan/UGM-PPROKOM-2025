n = int(input("Masukkan ukuran matriks identitas: "))

A = [
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
]

Array =[[1 if i==j 
         else 0 
          for j in range(n)] for i in range(n)]
print(f"Matriks ukuran {n}x{n} :",Array)