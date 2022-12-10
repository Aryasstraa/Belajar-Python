import os
os.system('cls')

def suhu(x):
  rea = x * 4/5
  fah = (x * 9/5)+32
  kel = x + 273
  print ("\n""Konversi suhu dalam Reamur     : ", rea,  "°R.")
  print ("Konversi suhu dalam Fahrenheit : ", fah,  "°F.") 
  print ("Konversi suhu dalam Kelvin     : ", kel,  "°K. ")


a = int(input("Masukan suhu dalam Celcius     : ",))
suhu(a)
