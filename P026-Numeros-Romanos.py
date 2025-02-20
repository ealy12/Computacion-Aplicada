# Realizar un programa que pida un número entre 1 y 10 y muestre su equivalente en número romano ( I, II, III, IV, V,VI, VII, VIII, IX, X).

import os;os.system('cls')
print('Dame un numero entre el 1 al 10, para darte el equivalente en numero Romano: ')
n = int(input())
if n == 1:
    print("Es I")
elif n == 2:
    print('Es II')
elif n == 3:
    print('Es III')
elif n == 4:
    print('Es IV')
elif n == 5:
    print('Es V')
elif n == 6:
    print('Es VI')
elif n == 7:
    print('Es VII')
elif n == 8:
    print('Es VIII')
elif n == 9:
    print('Es IX')
elif n == 10:
    print('Es X')
else: 
    print("Numero fuera de rango")