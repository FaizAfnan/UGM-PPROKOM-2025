import Konversi_suhu as ks

print("Program Konversi Suhu")
print("1. Celsius ke Fahrenheit")
print("2. Fahrenheit ke Celsius")
print("3. Celsius ke Kelvin")
print("4. Kelvin ke Celsius")
print("5. Fahrenheit ke Kelvin")
print("6. Kelvin ke Fahrenheit")

pilihan = input("Pilih konversi (1-6): ")

suhu = float(input("Masukkan nilai suhu: "))

if pilihan == '1':
    hasil = ks.celsius_ke_fahrenheit(suhu)
    print(f"{suhu} Celsius = {hasil} Fahrenheit")
elif pilihan == '2':
    hasil = ks.fahrenheit_ke_celsius(suhu)
    print(f"{suhu} Fahrenheit = {hasil} Celsius")
elif pilihan == '3':
    hasil = ks.celsius_ke_kelvin(suhu)
    print(f"{suhu} Celsius = {hasil} Kelvin")
elif pilihan == '4':
    hasil = ks.kelvin_ke_celsius(suhu)
    print(f"{suhu} Kelvin = {hasil} Celsius")
elif pilihan == '5':
    hasil = ks.fahrenheit_ke_kelvin(suhu)
    print(f"{suhu} Fahrenheit = {hasil} Kelvin")
elif pilihan == '6':
    hasil = ks.kelvin_ke_fahrenheit(suhu)
    print(f"{suhu} Kelvin = {hasil} Fahrenheit")
else:
    print("Pilihan tidak valid.")