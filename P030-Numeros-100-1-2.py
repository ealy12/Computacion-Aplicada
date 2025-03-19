# Imprime numeros de 1-100
import os;os.system('cls')
n = int(input('Hasta donde '))
c = n

while c >= 1:
    print(c, end=' ')
    c -= 1
else:
    print('\n Valor final de C', c)
print('Proceso terminado')