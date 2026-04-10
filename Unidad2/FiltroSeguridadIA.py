LIMITE_SUPERIOR= 100.0
LIMITE_INFERIOR= 0.0
LECTURA=float(input("Ingrese la lectura del sensor térmico: "))
if LECTURA > LIMITE_INFERIOR:
    dato_normalizado=  LECTURA / LIMITE_SUPERIOR
    print("Señal aceptada. Valor normalizado para el modelo:", dato_normalizado)
elif LECTURA > LIMITE_SUPERIOR:
    print("invalido")
else: 
    print("Error: Lectura fuera de rango. La señal se considera ruido")
print("Fin del proceso de filtrado de datos.")
