#repasa 

print("--- Configuración de Sensores de Proximidad ---")
sensores_distancia = []
for i in range(5):
    distancia = float(input(f"Ingrese la distancia del sensor {i+1} (en metros): "))
    sensores_distancia.append(distancia)

promedio = sum(sensores_distancia) / len(sensores_distancia)
print(f"\nPromedio de distancia: {promedio:.2f}m")

if promedio < 2.0:
    print("Aviso: Reduciendo velocidad global")


print("\n--- Configuración de Cámara IA (Matriz 3x3) ---")
camara_ia = []

for f in range(3):
    fila = []
    for c in range(3):
        brillo = int(input(f"Ingrese brillo para píxel [{f}][{c}] (0-255): "))
        if brillo > 255:
            brillo = 255
        fila.append(brillo)
    camara_ia.append(fila)
print("\nMatriz de Visión:")
for fila in camara_ia:
    print(f"[ {fila[0]:>3} {fila[1]:>3} {fila[2]:>3} ]")

puntos_brillantes = 0
for fila in camara_ia:
    for pixel in fila:
        if pixel > 200:
            puntos_brillantes += 1

print(f"\nTotal de puntos brillantes detectados (>200): {puntos_brillantes}")
