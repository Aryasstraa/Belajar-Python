import os
from time import time
os.system('cls')

phi=3.14
r=float(input("Masukan Jari-Jari :"))
l=phi*r*r

if r>=0:print("Luas lingkaran dengan Jari-Jari",r,"cm adalah",l,"cm")
else:print("Tolong masukan angka yang benar")

Masukan=int(input("Masukan angka dari 0 sampai  100:"))

if Masukan >=0 and Masukan <=54:print("ini adalah langkah E")
elif Masukan  >=55 and Masukan <=64:print("ini adalah langkah D")
elif Masukan >=65 and Masukan <=74:print("ini adalah langkah C")
elif Masukan  >=75 and Masukan <=84:print("ini adalah langkah B")
elif Masukan  >=85 and Masukan <=100:print("ini adalah langkah A")
else:print("Tolong masukan angka dari 0 sampai 100")