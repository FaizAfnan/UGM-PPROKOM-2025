import produk as p
import transaksi as t

print("==APLIKASI PENJUALAN TOKO PYTHON==")
print("\n==DAFTAR PRODUK==")
p.tampil_produk()
pilihan_produk = input("Pilih produk (1-3): ")
jumlah_beli = input("Masukkan jumlah beli: ")

if pilihan_produk == "1":
    nama_produk = p.produk[0]
    harga_produk = p.harga[0]
elif pilihan_produk == "2":
    nama_produk = p.produk[1]
    harga_produk = p.harga[1]
elif pilihan_produk == "3":
    nama_produk = p.produk[2]
    harga_produk = p.harga[2]
else:
    print("Pilihan produk tidak valid. Silakan coba lagi.")

print("\n==STRUK PEMBAYARAN==")
print (f"Produk         : {nama_produk}")
print (f"Harga Satuan   : Rp{harga_produk}")
print (f"Jumlah Beli    : {jumlah_beli}")
print (f"Subtotal       : Rp{t.subtotal(int(jumlah_beli), harga_produk)}")
print (f"Diskon         : Rp{t.diskon(t.subtotal(int(jumlah_beli), harga_produk))}")
print (f"Total Bayar    : Rp{t.total_bayar(subtotal, diskon)}")

pilihan_lanjut = input("Apakah Anda Ingin Melanjutkan Transaksi? (y/n): ")
while True:
    if pilihan_lanjut == "y":
        continue
    elif pilihan_lanjut == "n":
        print("Terima kasih telah berbelanja di Toko Python!")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
        break