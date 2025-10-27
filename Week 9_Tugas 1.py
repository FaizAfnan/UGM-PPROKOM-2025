A = [
    [   
        [1, 2, 3],
        [4, 5, 6]
    ],
    [   
        [7, 8, 9],
        [10, 11, 12]
    ]
]

print("Semua elemen pada lapisan 1 :", A[0])
print("Elemen kolom terakhir dari setiap baris dan lapisan:")
for i in range(len(A)):          
    for j in range(len(A)):  
        print(f"Lapisan {i+1}, Baris {j+1} -> ", A[i][j][2])

