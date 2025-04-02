# Calcular el factorial de m numeros enteros

print('Calcula e imprime el factorial de m numeros enteros')
import os;os.system('cls')

m = int(input('Hasta que numero deseas el factorial? '))
# n = int(input('Dame un numero entero: '))


for x in range(1,m+1):
    f = 1
    sec = ""
    for i in range(1,x+1):
        f=f*i
        sec = sec + str(i)
        if i<x:
            sec = sec + " * "
    print(f'{x}! = {sec} es: {f:,}')