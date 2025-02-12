#Hipotenusa de un triangulo
import os;os.system('cls')
import math as mt

L1 = int(input("Ingresa la longitud del cateto adyacente: "))
L2 = int(input("Ingresa la longitud del cateto opuesto: "))

Hip = mt.sqrt(mt.pow(L1,2)+mt.pow(L2,2))

print(f"La hipotenusa del triangulo es: {Hip:.4f}")