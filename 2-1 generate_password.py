import random

kecil = "abcdefghijklmnopqrstuvwxyz"
besar = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
angka = "1234567890"
simbol = "!@#$%^&*():;'<>,/?`~[]\|}{"

string = kecil + besar + angka + simbol
length = 8
password = "".join (random.sample(string, length))

print("password : " + password)