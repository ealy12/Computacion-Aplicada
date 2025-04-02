# Imprime de manera inicial un cuadro de asteriscos
import os
os.system('cls')
while(True):
    n = int(input('Cuantos renglones? '))
    c = input('Caracter? ')
    for i in range(1,n+1):  
        for j in range(1,i+1):
            print(c, end='')
        print()
    if input('Deseas otra tabla S/N? ').upper()=='N':
        break
print('Proceso terminado')