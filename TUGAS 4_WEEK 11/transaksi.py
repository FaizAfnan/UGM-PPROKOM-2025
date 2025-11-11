def subtotal (jumlah, harga):
    subtotal = jumlah * harga
    return subtotal

def diskon (subtotal):
    diskon = subtotal * 0.1
    return diskon

def total_bayar (subtotal, diskon):
    total_bayar = subtotal - diskon
    return total_bayar