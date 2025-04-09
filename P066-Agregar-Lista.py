#ejemplificar el agregado de elementos a una lista de numeros

import os; 
os.system('cls')

print('Agregar elementos a una lista existente')
nums= [80.3,12.5,60.2,20.4]
print(f'La lista completa es: {nums}, tiene: {len(nums)} elementos')

print('Agregar elementos al final de la lista usando el metodo append()')
nums.append(90)
nums.append(100)
print(f'La lista completa es: {nums}, tiene: {len(nums)} elementos')

print('\nInsertar dos numeros en una posicion determinda usando el metodo insert()')
nums.insert(3,70)
print(f'La lista completa es: {nums}, tiene: {len(nums)} elementos')

print('Insertar mas de un elemento a la vez, en una posicion determinada usando un slice')
nums [5:5] = [75,76,77]
print(f'La lista completa es: {nums}, tiene: {len(nums)} elementos')