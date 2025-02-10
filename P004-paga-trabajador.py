# Calcular la paga total de un trabajador en base a las horas trabajadas y la paga por hora
# entrada: nombre, horas, paga
# salida: pagabruta(antes de impuesto),impuesto(paga*tasa),paganeta(paga despues de impuesto)

print('Calculando la paga de un trabajador \n')

# entrada de datos
nombre = input('Nombre del trabajador:  ')
horas = int(input('Horas trabajadas:  '))
paga = float(input('Paga x hora trabajada:  '))
tasa = 0.03

# Calculos
pagabruta = horas*paga
impuesto = pagabruta * tasa
paganeta = pagabruta-impuesto

# Salida
print('\n Resumen de pagos')
print(f'El trabajador {nombre}, trabajo {horas}, a una paga de {paga} pesos, a una tasa de {tasa} de impuesto ')
print(f'paga bruta(antes de inpuesto): {pagabruta:,.2f}')
print(f'Impuesto:  {impuesto:,.2f}')
print(f'PagaNeta(Despues de impuesto):  {paganeta:,.2f}')