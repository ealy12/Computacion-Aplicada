#Ejemplifica las operaciones matematicas basicas

import os;os.system('cls')

#Dato de prueba
#x = 10.5
#y = 2.5

x = float(input('Valor de x: '))
y = float(input('Valor de y: '))

suma = x + y
rest = x - y
mult = x * y
div = x / y
res = x % y
pot = x ** y
dive = x // y

print(f'Suma: {suma}\n Resta: {rest}\n Multiplicacion: {mult}\n division:{div} ')
print(f'Residuo: {res}\n Potencia: {pot}\n Division entera: {dive}\n')
