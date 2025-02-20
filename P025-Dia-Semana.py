# Dado un numero entero entre 1 y 7, se desea mostrar con letra el día de la semana correspondiente, 1 es domingo, 2 es lunes y así hasta 7 es viernes.
import os;os.system('cls')
print('Imprime dias de las semana de acuerdo a un numero 1(LUNES)- 7(Domingo)')
dia = int(input())
if dia == 1:
    print("Es lunes")
elif dia == 2:
    print('Es martes')
elif dia == 3:
    print('Es miercoles')
elif dia == 4:
    print('Es jueves')
elif dia == 5:
    print('Es viernes')
elif dia == 6:
    print('Es sabado')
elif dia == 7:
    print('Es domingo')
else:
    print('Numero incorrecto, dame uno en valor del rango establecido')