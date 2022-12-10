
import os
os.system('cls')

varperkalian = int(input("Masukan angka perkalian  : "))
varstart = int(input("Masukan angka Start  : "))
varfinish = int(input("Masukan angka Finish : "))
for i in range(varstart,varfinish +1):
    print(varperkalian, " x ", i ," = ", varperkalian * i)
    
# while (varstart <= varfinish):
#     print(varstart)
#     varstart += 1