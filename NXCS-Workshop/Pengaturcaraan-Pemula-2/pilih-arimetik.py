# Program untuk memilih operasi aritmetika

def calculator():
    print("Pilih operasi aritmetika:")
    print("1. Penjumlahan (+)")
    print("2. Pengurangan (-)")
    print("3. Perkalian (*)")
    print("4. Pembagian (/)")
    print("5. Pembagian Bulat (//)")
    print("6. Modulus (%)")
    print("7. Pangkat (**)")
    
    pilihan = input("Masukkan pilihan (1-7): ")
    
    a = float(input("Masukkan angka pertama: "))
    b = float(input("Masukkan angka kedua: "))
    
    if pilihan == "1":
        hasil = a + b
        operasi = "+"
    elif pilihan == "2":
        hasil = a - b
        operasi = "-"
    elif pilihan == "3":
        hasil = a * b
        operasi = "*"
    elif pilihan == "4":
        hasil = a / b
        operasi = "/"
    elif pilihan == "5":
        hasil = a // b
        operasi = "//"
    elif pilihan == "6":
        hasil = a % b
        operasi = "%"
    elif pilihan == "7":
        hasil = a ** b
        operasi = "**"
    else:
        print("Pilihan tidak valid!")
        return
    
    print(f"Hasil: {a} {operasi} {b} = {hasil}")

# Jalankan kalkulator
calculator()
