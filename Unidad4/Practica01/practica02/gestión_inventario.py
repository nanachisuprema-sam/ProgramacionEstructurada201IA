import numpy as np
# 1. DEFINICIÓN DE UN VECTOR
# Precios de los productos: [Poción, Espada, Escudo]
precios = np.array([50, 150, 100])
# 2. DEFINICIÓN DE UNA MATRIZ
# Cantidades que tienen 3 usuarios diferentes
# Fila 0: Usuario A, Fila 1: Usuario B, Fila 2: Usuario C
inventarios = np.array([
 [5, 1, 0], # Usuario A: 5 pociones, 1 espada, 0 escudos
 [2, 0, 1], # Usuario B
 [10, 2, 2] # Usuario C
])
# 3. OPERACIONES SOBRE ARREGLOS
# Calcular cuánto dinero tiene cada usuario en objetos (Matriz x Vector)
riqueza_total = np.dot(inventarios, precios)
print("=== REPORTE DE ECONOMÍA DEL SERVIDOR ===")
print(f"Precios unitarios: {precios}")
print(f"Riqueza por usuario: {riqueza_total}")
print(f"El usuario más rico tiene: {np.max(riqueza_total)} monedas.")