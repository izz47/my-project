#Contoh 1
# Penukaran dari int ke str
nombor = 10
nombor_str = str(nombor)
print("Nombor sebagai teks: " + nombor_str)

# Penukaran dari str ke int
teks = "20"
teks_int = int(teks)
print("Hasil tambah: ", teks_int + 5)

# Penukaran dari int ke float
bilangan = 7
bilangan_float = float(bilangan)
print("Bilangan perpuluhan: ", bilangan_float)

######################################################

#Contoh 2 (Pengiraan Harga Selepas Diskaun)
# Minta pengguna memasukkan harga asal dan diskaun
harga_asal = input("Masukkan harga asal: ")
diskaun = input("Masukkan peratusan diskaun (%): ")

# Pastikan input adalah nombor sebelum diproses
if harga_asal.replace(".", "", 1).isdigit() and diskaun.replace(".", "", 1).isdigit():
    harga_asal = float(harga_asal)
    diskaun = float(diskaun)

    harga_akhir = harga_asal - (harga_asal * (diskaun / 100))
    print(f"Harga selepas diskaun: RM{harga_akhir:.2f}")
else:
    print("Sila masukkan nilai yang sah untuk harga dan diskaun!")

