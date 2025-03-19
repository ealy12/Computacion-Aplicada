# Suma numeros hasta dar 100

import os;os.system('cls')

c = 0
s = 0
while c < 200:
    c += 1
    s += c
    print(c, end=' ')
    if s >= 100:
        print('\n')
        break
else:
    print('\n Llegamos a la meta')
print(f'suma {s}, numero sumados para alcanzar la meta {c}')