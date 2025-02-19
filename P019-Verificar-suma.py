# Verifica si la suma de dos numeros es igual a un tercero 

import os;os.system('cls')
print('Verifica si la suma de dos numeros es igual a un tercero')
print('Dame 3 numero esteros, separados por un enter')
n1, n2, n3 = int(input()), int(input()), int(input())

if n1+n2==n3:
    print(f'{n1}+{n2}={n3} el primero mas el segundo es igual al tercero')
elif n1+n3==n2:
    print(f'{n1}+{n3}={n2} el primero mas el tercero es igual al segundo')
elif n2+n3==n1:
    print(f'{n2}+{n3}={n1} el segundo mas el tercero es igual al primero')
else:
    print("posiblemente son iguales o la suma de dos numeros no es igual al tercero")
