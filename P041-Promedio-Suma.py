# Se desea calcular la suma y el promedio de una serie de números introducidos por el teclado hasta introducir 0,
# además deberá contar cuantos números se introdujeron. El proceso debe poder repetirse hasta que el usuario lo
# decida.
import os;os.system('cls')
opcion = 0
sumatoria = 0
i = 0
while opcion == 0:
    num = int(input('Dame el numero a sumar: '))
    i = i + 1
    sumatoria = sumatoria + num
    promedio = sumatoria / i
    opcion = int(input('Deseas continuar la sumatoria? escribe 0 para si: '))

print(f'La sumatoria es: {sumatoria} y el numero de datos introducios es: {i}')
print('el promedio optenido es: ', promedio)