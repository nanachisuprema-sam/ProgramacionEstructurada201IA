# 1. IMPORTACIÓN (Biblioteca Estándar)
import datetime
def calcular_dias_restantes(fecha_evento_str):
 """
 Función que utiliza la biblioteca datetime para calcular la
 diferencia entre hoy y una fecha futura.
 """
 # Obtener la fecha y hora actual del sistema (Función externa)
 ahora = datetime.datetime.now()

 # Convertir un texto (string) a un objeto de fecha real
 fecha_evento = datetime.datetime.strptime(fecha_evento_str, "%d/%m/%Y")

 # Operación entre objetos de tiempo (Parámetros de salida implícitos)
 diferencia = fecha_evento - ahora

 return diferencia.days
# --- Programa Principal ---
# Definimos la fecha de nuestro próximo torneo en Discord (Día/Mes/Año)
fecha_torneo = "15/05/2025"
# Invocación y paso de parámetros
dias = calcular_dias_restantes(fecha_torneo)
print("=== SISTEMA DE EVENTOS DISCORD ===")
print(f"Fecha del evento: {fecha_torneo}")
print(f"Estado: Faltan exactamente {dias} días para el inicio.")