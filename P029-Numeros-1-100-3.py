# Imprime numeros de 1-100
import os;os.system('cls')
n = int(input('Hasta donde '))
d = int(input('Incrementos '))
c = 0

while c <= n:
    print(c, end=' ')
    c += d
else:
    print('\n Valor final de C', c)
print('Proceso terminado')