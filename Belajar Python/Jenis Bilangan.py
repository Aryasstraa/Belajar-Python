import os
os.system('cls')

b = int(input("Masukan Bilangan: "))

if b>0:
    print(b, "Adalah Positif")
elif b==0:
    print(b, "Adalah Netral")
else:
    print(b,"Adalah Negatif")