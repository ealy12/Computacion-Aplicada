# Se desea calcular el volumen de un cilindro dado su radio y altura

import os;os.system('cls')
import math as m

print('Ingresa las dimensiones del cilindro en centimetros\n')

radio =  int(input('radio :'))
altura = int(input('altura :'))

vol =  m.pi*(radio**2)*altura

print(f'El volumen del cilindro es: {vol:.4f} centimetros cubicos')