#ejercicio de induccion pago de nómina
numero_horas= float(input("ingrese el numero de horas trabajadas: "))
tarifa_hora= float(input("ingrese la tarifa pot hora: "))
nombre_empleado= input("ingrese nombre del empleado: ")

#horas superiores a 35 pagan extra
if numero_horas > 35:
    horas_extra = numero_horas -35
    pago_bruto= (35 * tarifa_hora) + (horas_extra * tarifa_hora * 1.5)
else:
    pago_bruto= numero_horas * tarifa_hora

#calculo impuesto

if pago_bruto <=2000:
    impuesto= 0
elif pago_bruto <= 2220:
    impuesto= (pago_bruto - 2000) * 0.20
else:
    impuesto= (pago_bruto - 2000) * 0.30 + 220 *0.20

pago_neto= pago_bruto - impuesto
#muestra resultados
print(f"empleado: {nombre_empleado}")
print(f"pago_bruto: ${pago_bruto:2f}")
print(f"impuesto: ${impuesto:.2f}")
print(f"pago neto: ${pago_neto:.2f}")