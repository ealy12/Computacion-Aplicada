# Verificar si la suma de dos numeros enteros es igual a la tercera

import os;os.system('cls')

print('Verificar si la suma de dos numeros enteros es igual a la tercera')

print('Dame 3 numero esteros, separados por un enter')
n1, n2, n3 = int(input()), int(input()), int(input())

if n1+n2==n3:
    print('La suna de los dos primeros es igual al tercero \n')
else:
    print("La suma de los dos primeros numeros no es igual al tercero \n")
    
print('Gracias por utilizar este programa \n')
