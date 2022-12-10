import os
os.system('cls')

k = str(input("Masukan karakter  : "))
n = int(input("Masukan jumalah  : "))

for i in range(1,n+1):
    for j in range(1,i+1):
        print(k, end =  "")
    print()


for i in reversed(range(1,n+1)):
    for j in reversed(range(1,i+1)):
        print(k, end =  "")
    print()