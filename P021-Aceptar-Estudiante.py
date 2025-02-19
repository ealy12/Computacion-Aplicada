# Aceptacion de estudiante a universidad

import os;os.system('cls')
print("Bienvenido a la UAZ")
nombre=input('Dame tu nombre: ')
edad=int(input('Dame tu edad: '))
if edad<18:
    print('Solo se aceptan personas mayores de 18 años')
else:
    print('Dame dos calificaciones')
    c1, c2 = int(input()), int(input())
    if c1 < 8 or c2 < 8:
        print('Lo sentimos, Solo se aceptan calificaciones mayores a 8')
    else:
        print(f'{nombre} bienvenido a la Universidad Autonoma de Zacatecas, tu edad {edad} y calificaciones {c1} y {c2} lo permiten')