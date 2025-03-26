# Calcular el número mayor de una serie de números introducidos por el teclado, el proceso se detiene al introducir
# 0. El proceso debe poder repetirse hasta que el usuario lo decida.
import os;os.system('cls')


opcion = 's'

while opcion == 's':
    mayor = 0  
    print('Introduce números (0 para terminar): ')
    while True:
        num = int(input(' '))
        if num == 0:
            break  
        if mayor is None or num > mayor:
            mayor = num 
    if mayor is not None:
        print(f'El número mayor ingresado es: {mayor}')
    else:
        print('No ingresaste ningún número válido.')
    opcion = input('¿Deseas repetir el proceso? (s/n): ').lower()