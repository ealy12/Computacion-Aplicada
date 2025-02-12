# Dada una temperatura en grados celcius, obtener su equivalente en grados farenheit

import os;os.system('cls')
TempC = int(input('Ingresa la temperatura en grados Celcius para convetir a grados Fahrenheit: '))

ConverF = (TempC*(9/5))+32

print(f'{TempC}°C equivale a {ConverF}°F')