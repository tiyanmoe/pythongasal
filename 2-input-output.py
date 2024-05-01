# Input adalah masukan yang kita berikan ke program.
# Program akan memprosesnya dan menampilkan hasil outputnya.
# Input, proses, dan output adalah inti dari semua program komputer.

# SINTAKSIS 
# nama_variabel = input("Sebuah Teks") 

# CONTOH
# Mengambil input
nama = input("Siapa nama kamu: ")
umur = input("Berapa umur kamu: ")

# Menampilkan output
print("Hello", nama,"umur kamu adalah", umur,"tahun")

nama = input("Inputkan nama: ")
umur = input("Inputkan umur: ")
tinggi = input("Inputkan tinggi badan: ")

print ("Hello %s, saat ini usiamu %i tahun dan tinggi badanmu %f cm" % (nama, umur, tinggi))