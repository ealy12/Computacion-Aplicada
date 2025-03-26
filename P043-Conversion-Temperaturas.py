# Se desea calcular la temperatura convertida de grados centígrados a grados farenheit de un rango de valores
# introducidos por el usuario, es decir el usuario introduce la temperatura inicial y la temperatura final en grados
# centígrados y el programa realiza la conversión a farenheit incrementando el valor inicial en 1, hasta llegar al valor
# final. El proceso debe poder repetirse hasta que el usuario lo decida.
import os;os.system('cls')
opcion = 's'
while opcion == 's':
    Vini = int(input('Dame el valor inicial de la conversion en centigrados: '))
    VFin = int(input('Dame el valor final de la conversion en centigrados: '))
    acumulador = 0
    acumulador = Vini
    while acumulador <= VFin:
        farenheit = (acumulador * 1.8) + 32
        print(f'El valor de grados centigrados es: {acumulador} y el valor de grados farenheit es: {farenheit}')
        acumulador = acumulador + 1
    opcion = input('Deseas realizar otra conversion? (s/n): ').lower()