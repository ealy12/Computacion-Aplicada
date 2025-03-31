# numeros del 100 al 1 usando ciclo for

import os;os.system('cls')

x= int(input('Desde donde quieres comenzar: '))
i= int(input('incremento: '))

for n in range(x,0,-i):
    print(n, end= ' ')
print('\nLlegamos al final')