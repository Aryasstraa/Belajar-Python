import os
os.system('cls')

a=int(input("masukan Start : "))
b=int(input("masukan Finish : "))

if (a<b):
    for i in range(a,b+1):
        print(i)
else:    
    for i in reversed(range(b,a+1)):
        print(i)