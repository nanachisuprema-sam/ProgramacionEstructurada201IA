patron_maestro = [1, 0, 1, 1, 0]

print("ESCÁNER BIOMÉTRICO DE IA\n")

lectura_sensor = []
for i in range(1, 6):
    bit = int(input(f"Ingrese bit {i}: "))
    lectura_sensor.append(bit)

coincidencias = 0
for posicion in range(5):
    if lectura_sensor[posicion] == patron_maestro[posicion]:
        coincidencias += 1

similitud = (coincidencias / 5) * 100

print(f"\nSimilitud obtenida: {similitud}%")

if similitud == 100:
    print("ACCESO TOTAL: Identidad Verificada.")
elif similitud >= 60 and similitud < 100:
    print("ADVERTENCIA: Similitud parcial. Se requiere verificación manual.")
else:
    print("ALERTA: Intruso detectado. Sistema bloqueado.")
