# Imprime numeros de 1-100
import os;os.system('cls')
n = int(input('Hasta donde '))
c = 1

while c <= n:
    print(c, end=' ')
    c += 1
else:
    print('\n Valor final de C', c)
print('Proceso terminado')