import numpy as np
A = np.array([
    [2, 4, 6],
    [1, 3, 5]
])
B = np.array([
    [1, 1, 1],
    [2, 2, 2]
])

C = A + B
D = A - B
print("Hasil penjumlahan matriks A dan B :\n", C)
print("Hasil pengurangan matriks A dan B :\n", D)

Btranspose = np.transpose(B)
E = np.dot(A, Btranspose)
print("Hasil perkalian matriks A dan B transpose :\n", E)