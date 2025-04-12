# 📌 **Asas Python untuk Pemula**  

Selamat datang ke **Panduan Asas Python**! 🚀  
Di sini anda akan belajar konsep penting seperti:  
✅ **Operator Aritmetik**  
✅ **Pembolehubah & Kaedah Asas**  
✅ **Operator Perbandingan & Logik**  
✅ **String Literals & Escape Sequences**  
✅ **Ekspresi Boolean & Operator Logik**  
✅ **Pernyataan Kawalan (`if`, `elif`, `else`)**  
✅ **Perulangan (`for`, `while` loops)**  
✅ **Mentakrif & Memanggil Fungsi**  

---

## 🔢 **1. Operator Aritmetik**  
Operator aritmetik digunakan untuk melakukan pengiraan matematik.  

| Operator | Keterangan | Contoh |
|----------|------------|--------|
| `+` | Penambahan | `5 + 3 = 8` |
| `-` | Penolakan | `10 - 4 = 6` |
| `*` | Pendaraban | `6 * 7 = 42` |
| `/` | Pembahagian | `20 / 5 = 4.0` |
| `//` | Pembahagian tanpa titik perpuluhan | `20 // 3 = 6` |
| `%` | Modulus (baki pembahagian) | `10 % 3 = 1` |
| `**` | Pemangkatan | `2 ** 3 = 8` |

📌 **Contoh Kod:**  
```python
a = 10
b = 3
print(a + b)  # Output: 13
print(a // b)  # Output: 3

🏷 2. Pembolehubah & Kaedah Asas

Pembolehubah digunakan untuk menyimpan data dalam Python.

📌 Contoh:

nama = "Ali"
umur = 25
tinggi = 1.75

print(f"Nama: {nama}, Umur: {umur}, Tinggi: {tinggi}m")

📌 Jenis Data dalam Python:

    int → Nombor bulat (umur = 25)
    float → Nombor perpuluhan (tinggi = 1.75)
    str → Teks (nama = "Ali")
    bool → Boolean (is_student = False)

⚖️ 3. Operator Perbandingan & Logik

Operator perbandingan digunakan untuk membandingkan dua nilai.
Operator	Keterangan	Contoh
==	Sama dengan	5 == 5 → True
!=	Tidak sama dengan	3 != 4 → True
>	Lebih besar	10 > 5 → True
<	Lebih kecil	7 < 3 → False
>=	Lebih besar atau sama	5 >= 5 → True
<=	Lebih kecil atau sama	2 <= 4 → True

📌 Operator Logik:
Operator	Keterangan	Contoh
and	Kedua-dua syarat mesti benar	(5 > 2 and 10 < 20) → True
or	Salah satu syarat benar	(5 > 2 or 10 > 50) → True
not	Membalikkan nilai boolean	not (5 > 2) → False

📌 Contoh Kod:

x = 10
y = 5
print(x > y and y < 10)  # Output: True

🔤 4. String Literals & Escape Sequences

📌 Escape Sequences:
Escape	Makna
\n	Baris baru
\t	Tab (jarak besar)
\\	Backslash

📌 Contoh Kod:

teks = "Hello, dunia!\nSelamat datang ke Python!"
print(teks)

✅ 5. Ekspresi Boolean & Operator Logik

Boolean hanya mempunyai dua nilai: True atau False.

📌 Contoh Kod:

a = True
b = False

print(a and b)  # Output: False
print(a or b)   # Output: True
print(not a)    # Output: False

🎯 6. Pernyataan Kawalan (if, elif, else)

Digunakan untuk membuat keputusan dalam kod.

📌 Contoh Kod:

umur = 18

if umur >= 18:
    print("Anda sudah cukup umur untuk mengundi!")
elif umur == 17:
    print("Tunggu satu tahun lagi.")
else:
    print("Anda masih terlalu muda untuk mengundi.")

🔄 7. Perulangan (for & while Loops)

Perulangan digunakan untuk mengulangi kod.

📌 for loop:

for i in range(1, 6):  # Ulang dari 1 hingga 5
    print(f"Nombor: {i}")

📌 while loop:

x = 0
while x < 5:
    print(f"x sekarang: {x}")
    x += 1  # Tambah nilai x

🎭 8. Mentakrif & Memanggil Fungsi

Fungsi membantu dalam mengatur kod dan mengelakkan pengulangan.

📌 Contoh Kod:

def salam(nama):
    return f"Hai, {nama}! Selamat datang."

print(salam("Aiman"))

✅ Bagaimana ia berfungsi?

    def salam(nama): → Mendefinisikan fungsi bernama salam.
    return f"Hai, {nama}! ..." → Mengembalikan teks dengan nama.
    print(salam("Aiman")) → Memanggil fungsi dan mencetak hasilnya.
