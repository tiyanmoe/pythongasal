# Operator Logika
# Operator logika digunakan untuk membuat operasi logika, seperti logika AND, OR, dan NOT.

# CONTOH 1
a = True
b = False

# Logika AND
c = a and b
print "%r and%r = %r" % (a,b,c)

# Logika OR
c = a or b
print "%r or %r = %r" % (a,b,c)

# Logika Not
c = not a
print "not %r  = %r" % (a,c)


# CONTOH 2
p = True
q = False
print("Operator Logika:")
print("\nBerikut adalah hasilnya:")
print("p and q:", p and q)
print("p or q:", p or q)
print("not p:", not p)
print("not q:", not q)


# PROGRAM 2 
# Input informasi dari pengguna
usia = int(input("Masukkan usia Anda: "))
pengalaman_kerja = int(input("Masukkan tahun pengalaman kerja Anda: "))

# Menentukan kelayakan berdasarkan usia dan pengalaman kerja menggunakan operator logika
if usia >= 25 and pengalaman_kerja >= 3:
    kelayakan = "Anda layak untuk melamar pekerjaan ini."
else:
    kelayakan = "Maaf, Anda belum memenuhi syarat kelayakan."

# Menampilkan hasil kelayakan
print(kelayakan)