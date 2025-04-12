nama = input("Masukkan nama anda: ")
print("Hai, " + nama + "!")

#####################################
#Contoh lain termasuk masa
import datetime

nama = input("Masukkan nama anda: ")

# Dapatkan jam semasa
jam_semasa = datetime.datetime.now().hour

# Tentukan ucapan berdasarkan waktu
if 5 <= jam_semasa < 12:
    ucapan = "Selamat pagi"
elif 12 <= jam_semasa < 18:
    ucapan = "Selamat petang"
else:
    ucapan = "Selamat malam"

# Cetak ucapan dengan nama pengguna
print(f"{ucapan}, {nama}!")
