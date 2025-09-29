buah_buahan = {
    "apel": 15000,
    "jeruk": 10000,  
    "anggur" : 25000
}

print("harga jeruk adalah: ", buah_buahan["jeruk"])

buah_buahan["mangga"] = 12000
print("setelah ditambah mangga:", buah_buahan)

buah_buahan["anggur"] = 20000
print("setelah diubah harga anggur:", buah_buahan)

del buah_buahan["jeruk"]
print("setelah dihapus jeruk:", buah_buahan)

print("\nBuah-buahan yang tersedia: ")
for buah, harga in buah_buahan.items():
    print(f"{buah.title()}: Rp {harga}")