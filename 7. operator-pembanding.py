# PROGRAM 1 :
# Input dua bilangan dari pengguna
# num1 = float(input("Masukkan bilangan pertama: "))
# num2 = float(input("Masukkan bilangan kedua: "))

# # Membandingkan bilangan menggunakan operator perbandingan
# if num1 > num2:
#     print(f"{num1} lebih besar dari {num2}")
# elif num1 < num2:
#     print(f"{num1} lebih kecil dari {num2}")
# else:
#     print(f"{num1} sama dengan {num2}")



# PROGRAM 2
# Input nilai ujian dari pengguna
nilai_ujian = float(input("Masukkan nilai ujian: "))

# Menentukan kategori berdasarkan nilai ujian menggunakan operator perbandingan
if nilai_ujian >= 90:
    kategori = "A"
elif nilai_ujian >= 80:
    kategori = "B"
elif nilai_ujian >= 70:
    kategori = "C"
elif nilai_ujian >= 60:
    kategori = "D"
else:
    kategori = "E"

# Menampilkan hasil kategori
print(f"Nilai ujian Anda adalah {nilai_ujian}, sehingga masuk kategori: {kategori}")

# Penjelasan:

# Program ini meminta pengguna untuk memasukkan nilai ujian.
# Kemudian, program menggunakan operator perbandingan (>=) untuk membandingkan nilai ujian dengan beberapa batas tertentu.
# Jika nilai ujian memenuhi kondisi pertama (nilai_ujian >= 90), maka kategori diatur menjadi "A".
# Jika nilai ujian tidak memenuhi kondisi pertama, program melanjutkan ke kondisi berikutnya (nilai_ujian >= 80) dan seterusnya.
# Jika nilai ujian tidak memenuhi semua kondisi, kategori diatur menjadi "E".
# Hasil kategori kemudian ditampilkan kepada pengguna.
# Dalam contoh ini, operator perbandingan (>=) digunakan untuk membandingkan nilai ujian dengan batas-batas tertentu. Jika kondisi perbandingan terpenuhi, program akan melakukan tindakan yang sesuai. Dengan demikian, operator perbandingan membantu program untuk membuat keputusan berdasarkan nilai yang diberikan oleh pengguna.
