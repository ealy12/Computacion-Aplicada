# Se desea calcular el promedio de 5 calificaciones introducidas por el usuario, luego evaluar el resultado e imprimir un mensaje de acuerdo al promedio obtenido
import os;os.system('cls')
print('Calculo de promedio de calificaciones')
print('Introduce 5 calificaciones para saber tu promedio: ')
c1, c2, c3, c4, c5 = int(input()), int(input()), int(input()), int(input()), int(input())
prom = (c1 + c2 + c3 + c4 + c5)/5
if prom > 0 and prom < 6:
    print(f'promedio: {prom} Quedas reprobado')
elif prom > 6 and prom <7:
     print(f'promedio: {prom} pasas de panzaso')
elif prom > 7 and prom <8:
    print(f'promedio: {prom} Muy bien, puedes mejorar')
elif prom > 8 and prom < 9:
    print(f'promedio: {prom} Excelente sigue asi')
elif prom >9 and prom <=10:
    print(f'promedio: {prom} Perfecto tu esfuerzo valió la pena')
