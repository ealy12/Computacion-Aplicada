#Se desea imprimir los números pares desde 100 hasta el número que el usuario decida (n), además deberá
# imprimirse la suma de esos números pares. El proceso debe poder repetirse hasta que el usuario lo decida.
import os;os.system('cls')

opcion = 's'
while opcion == 's':
    inicio = 100
    sumatoria = 0
    fin = int(input('Dame el numero hasta el cual deseas terminar: '))
    while inicio >= fin:
        if inicio % 2 == 0:
            print('Este numero es par', inicio)
            sumatoria = sumatoria +inicio
        inicio = inicio -1
    print('\n Suma de los pares: ', sumatoria)
    opcion = input('Deseas continuar? (s/n): ').lower()    
print('Proceso terminado')   
    