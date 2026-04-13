metros=float(input("¿A qué distancia está el objeto más cercano (en metros)"))
color=input("¿De qué color está el semáforo?verde/amarillo/rojo").lower()
p=input("¿Hay un peatón cruzando? (si/no)").lower()
if metros <= 5 or p == "si":
    print("¡FRENO DE EMERGENCIA ACTIVADO! Deteniendo el vehículo inmediatamente")
elif color == "rojo":
    print("Estado: Detenido. Esperando luz verde.")
elif color == "amarillo":
    print("Estado: Precaución. Reduciendo velocidad para detenerse.")
elif color == "verde" in color or metros >5 in metros:
    print("Estado: En movimiento. Todo despejado para avanzar.")
else:
    print("Error de lectura en sensores: Color de semáforo no reconocido.")

print("Monitoreo de sensores constante... Sistema activo.")