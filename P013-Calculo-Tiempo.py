#Calcular el equivalente de horas en dias, horas y minutos
import os;os.system('cls')
Horas = int(input('ingresa la cantidad de horas del cual quieres saber la equivalencia en dias, minutos y segundos: '))

Dia = Horas/24
Mes = Horas*60
seg = Mes*Horas

Equi = (f'{Horas} horas equivale a: \n'
          f'{Dia:.2f} días\n'
          f'{Mes} minutos\n'
          f'{seg} segundos\n'
         )

print(Equi)