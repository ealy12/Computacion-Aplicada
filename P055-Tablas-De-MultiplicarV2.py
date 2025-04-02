# Imprime las tablas de 1-10 hasta el 10

import os
os.system('cls')

n = int(input('Tablas del 1 al ?'))
m = int(input('Hasta donde? '))
for t in range(1,n+1):
    print(f'tabla del {t}')
    for i in range(1,m+1):
        print(f"{t} x {i} = {t * i}")
    print()