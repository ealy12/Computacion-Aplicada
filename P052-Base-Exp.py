# Dado un número entero base y un exponente exp, calcular la potencia de base elevado a exp

import os; os.system('cls')

b = int(input('Base: '))
e = int(input('Exponente: '))
r = 1

for _ in range(e):
    r = r * b
print(f'{b}^{e} = {r}')