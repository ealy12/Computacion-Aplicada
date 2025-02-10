# leer y mostrar datoscel

print('Leyendo datos del usuario, luego enviar un saludo')

nombre = input('dame tu nombre:    ')
edad = input('Dame tu edad:    ')
peso = float( input('Dame tu peso:   ')) #float convierta la cadena a flotante


print(f'{nombre} bienvenido al lenguaje python, tu edad es {edad} y tu peso es {peso}')
print('')
print(type(nombre))
print(type(edad))
print(type(peso))
