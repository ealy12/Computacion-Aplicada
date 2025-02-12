#Dividir un numero entero en 4 cifras

import os;os.system('cls')
print('Dividir un numero entero de 4 cifras en unidades, decenas, centenas, millares')

n = int(input('Dame un numero entero de 4 cifras: '))

#n = 145

u = n % 10
n = n // 10
d = n % 10
n = n // 10
c = n % 10
n = n //10
m = n

print(f'Digitos individuales del año:\nMillares: {m}\nCentenas: {c}\nDecenas: {d}\nUnidades: {u}')
print(f'Suma de los digitos individuales: {m+c+d+u}')