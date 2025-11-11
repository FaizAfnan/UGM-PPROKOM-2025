produk = ["Keyboard", "Mouse", "Flashdisk"]
harga = [150000, 80000, 50000]

def tampil_produk():
    for i in range(len(produk)):
        print(f"{i+1}. {produk[i]} - Rp{harga[i]}")
