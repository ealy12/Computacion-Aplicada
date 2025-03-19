# Imprime numeros de 1-100
import os;os.system('cls')
n = int(input('Hasta donde '))
d = int(input('decrementos '))
c = n

while c >= 1:
    print(c, end=' ')
    c -= d
else:
    print('\n Valor final de C', c)
print('Proceso terminado')