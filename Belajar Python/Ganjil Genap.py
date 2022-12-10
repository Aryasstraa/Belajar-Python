import os
os.system('cls')

a=int(input("masukan Start : "))
b=int(input("masukan Finish : "))

for i in range(a,b+1):
    if i % 2 ==0:
        print("%i genap" %i)
    else:
        print(("%i ganjil" %i))