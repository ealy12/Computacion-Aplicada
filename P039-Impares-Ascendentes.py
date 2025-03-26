# Se desea imprimir los números impares de forma ascendente desde 1 hasta el número que el usuario decida (n)
# además deberá imprimirse la suma de esos números impares. El proceso debe poder repetirse hasta que el usuario lo decida.

import os;os.system('cls')
inicio = 1
opcion = 's'
while opcion == 's':
    fin = int(input('Dame el numero hasta el cual lo quieres realizar: '))
    suma = 0
    numero = inicio
    while numero <= fin:
        if numero % 2 != 0:  # Verifica si es impar
            print(numero, end=" ")  # Imprime el número impar
            suma += numero  # Suma los números impares
        numero += 1  # Incrementa el número
    print('\nSuma de los números impares:', suma)
    opcion = input('Deseas continuar? (s/n): ').lower()
print('Proceso Terminado')