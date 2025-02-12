#Dados dos angulos de un triangulo, calcular el tercer angulo

import os;os.system('cls')

a1 = int(input('Ingresa el primer angulo del triangulo: '))
a2 = int(input('Ingresa el segundo angulo del triangulo: '))

a3 = 180-(a1+a2)

if a1+a2<180:
    print(f'El tercer ángulo es: {a3}')
else:
    print('Los datos son iguales o superan 180 grados, por favor ingresa los datos correctos')