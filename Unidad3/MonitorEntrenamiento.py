class MonitorEntrenamiento:
#estudia esto porque no le entendí
    def __init__(self, umbral=0.01):
        self.historial_errores = []
        self.umbral_convergencia = umbral

    def registrar_epoca(self, valor_error):
        # Guardamos el error en la lista
        self.historial_errores.append(valor_error)
        
        if valor_error < self.umbral_convergencia:
            print(f"[SISTEMA] Entrenamiento completado: Se alcanzó el objetivo de precisión.")
            return True
        return False

monitor = MonitorEntrenamiento(0.01)
epocas_totales = 5
contador = 0

print(f"Iniciando registro de {epocas_totales} épocas...")

while contador < epocas_totales:
    try:
        entrada = input(f"Ingrese el error de la época {contador + 1}: ")
        valor = float(entrada)
        
        if valor < 0:
            print("Error: El valor no puede ser negativo.")
            continue
            
        finalizado = monitor.registrar_epoca(valor)
        contador += 1
        
        if finalizado:
            break
            
    except ValueError:
        print("Error: Por favor, ingresa un número decimal válido (ej. 0.5).")

if monitor.historial_errores:
    print("\n--- RESULTADOS FINALES ---")
    print(f"Historial completo: {monitor.historial_errores}")
    
    promedio = sum(monitor.historial_errores) / len(monitor.historial_errores)
    mejor_error = min(monitor.historial_errores)
    
    print(f"Promedio de Error: {promedio:.4f}")
    print(f"Mejor Error: {mejor_error}")
