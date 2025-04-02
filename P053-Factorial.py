# Calcular el factorial de un numero entero 

print('Calcula e imprime el factorial de un numero entero')
import os;os.system('cls')
n = int(input('Dame un numero entero: '))

f = 1
sec = ""
for i in range(1,n+1):
    f=f*i
    sec = sec + str(i) + " * "
    if i<n:
        sec = sec + " * "
print(f'{n}! es: {f:,}')