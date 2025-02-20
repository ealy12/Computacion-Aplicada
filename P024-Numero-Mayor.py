# Dados tres números enteros, verificar cual es el mayor, ej: 10, 9 8, el mayor es 10, 11, 30, -1 el mayor es 30
import os;os.system('cls')
print('Dados tres números enteros, verificar cual es el mayor')
print('Dame 3 numeros enteros: ')
n1, n2, n3 = int(input()), int(input()), int(input())
if n1>n2 and n1>n3:
    print(f'\nEl numero {n1} es el mayor\n')
elif n2>n1 and n2>n3:   
     print(f'\nEl numero {n2} es el mayor\n')
else:
     print(f'\nEl numero {n3} es el mayor\n')