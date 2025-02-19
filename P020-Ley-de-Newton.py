# Calcular la fuerza, masa o aceleración, según lo elija el usuario, de acuerdo a la 2da ley de Newton

import os;os.system('cls')
print('# Calcular la fuerza, masa o aceleración, según lo elija el usuario, de acuerdo a la 2da ley de Newton')
print('(1) Calcular la fuerza')
print('(2) Calcular la masa')
print('(3) Calcular la aceleracion')

op=int(input('Eliga alguna opcion: '))

if op==1:
    print('Calculando fuerza')
    m=int(input('Dame la masa: '))
    a=int(input('Dame la aceleracion: '))
    f=m*a
    print(f'La fuerza es igual a: {f}')
elif op==2:
    print('Calculando masa')
    f=int(input('Dame la fuerza: '))
    a=int(input('Dame la aceleracion: '))
    m=f/a
    print(f'La masa es igual a: {m}')
elif op==3:
    print('Calculando aceleracion')
    f=int(input('Dame la fuerza: '))
    m=int(input('Dame la masa: '))
    a=f/m
    print(f'La aceleracion es igual a: {a}')
else:
    print('Introduzca una opcion valida')