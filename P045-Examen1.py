# Se desea llevar el control de la inscripción a un evento académico de la Universidad Patito. Se especifica: Tipo de usuario, paquete y cantidad.
# Tipo de usuario: [1] Alumno $100, [2] Trabajador $200, [3] Docente $500
# Tipo de paquete: [1] Solo conferencias $600, [2] Con eventos sociales $800, [3] Con kit de acceso $900

# Registro de usuario
CashA = 0
CashP = 0
Opciones = 's'
imporTot = 0
total = 0
import os;os.system('cls')



while Opciones == 's':
    import os;os.system('cls')
    
    print('Universidad Patio SA de CV')
    print('Sistema de inscripcion Congreso de Sistemas')
    usu = int(input('Dame el tipo de usuario [1] Alumno $100, [2] Trabajador $200, [3] Docente $500: '))
    paq = int(input('Dame el tipo de paquete [1] Solo conferencias $600, [2] Con eventos sociales $800, [3] Con kit de acceso $900: '))
    cant = int(input('Dame la cantidad: '))
    if usu == 1 and paq == 1: 
        Subtotal = (cant * 600) + (cant * 100)
        print(f'Tu pedido fue: {cant}, tipo de usuario: Alumno, tipo de paquete: Solo conferencias')
        if Subtotal > 5000:
            descuento = Subtotal * 0.20 
        else: 
            descuento = 0
        total = Subtotal - descuento
        print(f'Subtotal: {Subtotal} con un descuento de: {descuento} (0.20%) y un total de: {total}')
    elif usu == 1 and paq == 2:
        Subtotal = (cant * 800) + (cant * 100)
        print(f'Tu pedido fue: {cant}, tipo de usuario: Alumno, tipo de paquete: Con evento social')
        if Subtotal > 5000:
            descuento = Subtotal * 0.20 
        else: 
            descuento = 0
        total = Subtotal - descuento
        print(f'Subtotal: {Subtotal} con un descuento de: {descuento} (0.20%) y un total de: {total}')
    elif usu == 1 and paq == 3:
        Subtotal = (cant * 900) + (cant * 100)
        print(f'Tu pedido fue: {cant}, tipo de usuario: Alumno, tipo de paquete: Con KIT de acceso')
        if Subtotal > 5000:
            descuento = Subtotal * 0.20 
        else: 
            descuento = 0
        total = Subtotal - descuento
        print(f'Subtotal: {Subtotal} con un descuento de: {descuento} (0.20%) y un total de: {total}')
    elif usu == 2 and paq == 1:
        Subtotal = (cant * 600) + (cant * 200)
        print(f'Tu pedido fue: {cant}, tipo de usuario: Trabajador, tipo de paquete: Solo Conferencia')
        if Subtotal > 5000:
            descuento = Subtotal * 0.10 
        else: 
            descuento = 0
        total = Subtotal - descuento
        print(f'Subtotal: {Subtotal} con un descuento de: {descuento} (0.10%) y un total de: {total}')
    elif usu == 2 and paq == 2:
        Subtotal = (cant * 800) + (cant * 200)
        print(f'Tu pedido fue: {cant}, tipo de usuario: Trabajador, tipo de paquete: Con eventos sociales')
        if Subtotal > 5000:
            descuento = Subtotal * 0.10 
        else: 
            descuento = 0
        total = Subtotal - descuento
        print(f'Subtotal: {Subtotal} con un descuento de: {descuento} (0.10%) y un total de: {total}')
    elif usu == 2 and paq == 3:
        Subtotal = (cant * 900) + (cant * 200)
        print(f'Tu pedido fue: {cant}, tipo de usuario: Trabajador, tipo de paquete: Con KIT de acceso')
        if Subtotal > 5000:
            descuento = Subtotal * 0.10 
        else: 
            descuento = 0
        total = Subtotal - descuento
        print(f'Subtotal: {Subtotal} con un descuento de: {descuento} (0.10%) y un total de: {total}')
    elif usu == 3 and paq == 1:
        Subtotal = (cant * 600) + (cant * 500)
        print(f'Tu pedido fue: {cant}, tipo de usuario: Docente, tipo de paquete: Solo conferencia')
        if Subtotal > 5000:
            descuento = Subtotal * 0.05
        else: 
            descuento = 0
        total = Subtotal - descuento
        print(f'Subtotal: {Subtotal} con un descuento de: {descuento} (0.05%) y un total de: {total}')
    elif usu == 3 and paq == 2:
        Subtotal = (cant * 800) + (cant * 500)
        print(f'Tu pedido fue: {cant}, tipo de usuario: Docente, tipo de paquete: Con evento social')
        if Subtotal > 5000:
            descuento = Subtotal * 0.05
        else: 
            descuento = 0
        total = Subtotal - descuento
        print(f'Subtotal: {Subtotal} con un descuento de: {descuento} (0.05%) y un total de: {total}')
    elif usu == 3 and paq == 3:
        Subtotal = (cant * 900) + (cant * 500)
        print(f'Tu pedido fue: {cant}, tipo de usuario: Docente, tipo de paquete: kit de acceso')
        if Subtotal > 5000:
            descuento = Subtotal * 0.05
        else: 
            descuento = 0
        total = Subtotal - descuento
        print(f'Subtotal: {Subtotal} con un descuento de: {descuento} (0.05%) y un total de: {total}')
    else:
        print('Error de ejecucion, dame un numero valido')
    imporTot = imporTot + total
    
    Opciones = input('Deseas continuar? (s/n): ').lower() 
print(f'Importe total de venta: {imporTot}')
print('Proceso terminado')