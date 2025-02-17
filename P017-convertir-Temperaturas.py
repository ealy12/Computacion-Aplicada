# Convertir temperaturas de farenheit a centigrados y viceversa
import os;os.system('cls')

print('Convertir temperaturas de farenheit a centigrados y viceversa')
print('De centigrados a Farenheit...... (1)')
print('De Farenheit a Centigrados...... (2)')
op = int(input('Elige '))

if op == 1:
    print('Convirtiendo de Centigrados a Farenheit....')
    temp = float(input('Grados centigrados: '))
    res = (temp*9/5)+32
    print(f'{temp} Grados centigrados, equivale a {res} Grados farenheit')
else:
    print('Convirtiendo de Farenheit a Centigrados....')
    temp = float(input('Grados Farenheit: '))
    res = (temp-32)*5/9
    print(f'{temp} Grados Farenheit, equivale a {res} Grados Centigrados')