A = [
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
]

Array=[[
    1 if i==j
     else 0
      for j in range(len(A))] for i in range(len(A))]
print("Pola matriks :", Array)

n = int(input("Masukkan ukuran matriks identitas: "))
Array2 =[[1 if i==j 
         else 0 
          for j in range(n)] for i in range(n)]
print("Matriks baru :", Array2)