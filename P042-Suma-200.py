# Se desea calcular la suma de números introducidos por el usuario hasta que la suma sea >= 200, luego mostrar
# cuantos números fueron introducidos y la suma de estos. El proceso debe poder repetirse hasta que el usuario lo
# decida.

import os;os.system('cls')
opcion = 's'
while opcion == 's':
    import os;os.system('cls')
    sumatoria = 0
    i = 0
    while sumatoria < 200:
        num = int(input('Dame el numero a sumar: '))
        i = i + 1
        sumatoria = sumatoria + num 
    print(f'La sumatoria de los datos es: {sumatoria} y los datos introducidos fueron {i}')
    opcion = input('Deseas introducir mas numeros? (s/n): ').lower()