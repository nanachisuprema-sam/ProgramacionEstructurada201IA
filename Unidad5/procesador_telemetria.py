# ==========================================
# IMPORTACIÓN DE BIBLIOTECAS (Biblioteca Estándar)
# ==========================================
import sys

# ==========================================
# FUNCIONES GENERADAS POR IA (Auditoría Aplicada)
# ==========================================

def limpiar_lecturas(lista_datos):
    """
    Filtra una lista de lecturas de telemetría LIDAR.
    
    Elimina los valores atípicos menores a 0.0 o mayores a 100.0
    utilizando estructuras condicionales tradicionales.
    
    Argumentos:
    lista_datos (list): Lista de números flotantes (distancias).
    
    Retorna:
    list: Nueva lista con lecturas válidas entre 0.0 y 100.0 inclusive.
    """
    lista_filtrada = []
    for lectura in lista_datos:
        if lectura >= 0.0:
            if lectura <= 100.0:
                lista_filtrada.append(lectura)
    return lista_filtrada


def calcular_alertas(lista_filtrada, umbral_critico):
    """
    Cuenta las lecturas que se encuentran por debajo de un umbral crítico.
    
    Argumentos:
    lista_filtrada (list): Lista de lecturas limpias (flotantes).
    umbral_critico (float): Límite numérico para activar una alerta.
    
    Retorna:
    int: Cantidad total de lecturas que representan riesgo de colisión.
    """
    contador_alertas = 0
    for lectura in lista_filtrada:
        if lectura < umbral_critico:
            contador_alertas = contador_alertas + 1
    return contador_alertas


def generar_log_sistema(total_alertas):
    """
    Genera un mensaje de registro formateado según el sistema operativo actual
    y evalúa el nivel de riesgo en base al total de alertas.
    
    Argumentos:
    total_alertas (int): Número total de alertas detectadas.
    
    Retorna:
    str: Cadena de texto formateada con el estado del sistema.
    """
    sistema_operativo = sys.platform
    
    if total_alertas > 3:
        accion = "ABORTAR"
    else:
        accion = "PERMITIDA"
        
    log = "[" + sistema_operativo.upper() + "] Alertas críticas encontradas: " + str(total_alertas) + ". Acción: " + accion
    return log


# ==========================================
# PROGRAMA PRINCIPAL (Orquestación Manual)
# ==========================================
if __name__ == "__main__":
    # 1. Datos simulados de telemetría (con algunos errores de sensor)
    lecturas_raw = [12.5, -5.0, 88.2, 120.1, 1.2, 0.0, 45.6, 2.5]
    UMBRAL = 3.0
   
    print("=== SISTEMA DE TELEMETRÍA DE AGENTE AUTÓNOMO ===\n")
   
    # RESOLUCIÓN DEL RETO:
    # Invocación estructurada secuencial (Caja Negra)
    lecturas_limpias = limpiar_lecturas(lecturas_raw)
    alertas_detectadas = calcular_alertas(lecturas_limpias, UBRAL)
    log_final = generar_log_sistema(alertas_detectadas)
    
    # Impresión del resultado en pantalla
    print(log_final)


# ==========================================
# RETO DE EVALUACIÓN Y ENTREGABLE
# ==========================================
"""
1. EL PROMPT UTILIZADO

Para garantizar que la IA no utilizara atajos avanzados como la 'comprensión de listas' 
(list comprehension) o métodos avanzados de cadenas,
 se adaptó la plantilla base de la siguiente forma:

"Actúa como un programador experto en Python Estructurado Clásico. Escribe el código de tres funciones 
llamadas limpiar_lecturas, calcular_alertas y generar_log_sistema. 
[Insertar aquí las entradas, lógicas y salidas de la guía].
Restricciones estrictas:
1. No utilices programación orientada a objetos (POO).
2. No utilices manejo de excepciones.
3. NO utilices comprensión de listas, usa bucles for tradicionales con .append().
4. Gestiona los errores de datos usando condicionales if/else tradicionales.
5. Incluye la documentación de la función mediante un Docstring descriptivo."


2. TABLA DE PRUEBAS DE ESCRITORIO MANUAL (TRACE TABLE)
--------------------------------------------------------------------------------
Caso de Prueba Propuesto:
- lecturas_raw = [-10.5, 105.0, -1.0] (Todas las lecturas son erróneas/atípicas)
- UMBRAL = 5.0
- Sistema Operativo simulado: 'linux'

Paso 1: Ejecución de limpiar_lecturas([-10.5, 105.0, -1.0])

| Iteración | Variable 'lectura' | Condición (>=0.0 y <=100.0) | Variable 'lista_filtrada' |
|-----------|--------------------|-----------------------------|---------------------------|
| Inicio    | -                  | -                           | []                        |
| 1         | -10.5              | False                       | []                        |
| 2         | 105.0              | False                       | []                        |
| 3         | -1.0               | False                       | []                        |
Retorno de la función: []

Paso 2: Ejecución de calcular_alertas([], 5.0)

| Iteración | Variable 'lectura' | Condición (< 5.0) | Variable 'contador_alertas' |
|-----------|--------------------|-------------------|-----------------------------|
| Inicio    | -                  | -                 | 0                           |
El bucle for no se ejecuta porque la lista está vacía.
Retorno de la función: 0

Paso 3: Ejecución de generar_log_sistema(0)
- Variable 'sistema_operativo' toma el valor: 'linux' -> .upper() lo convierte en 'LINUX'
- Condición (total_alertas > 3) -> 0 > 3 es False.
- Variable 'accion' toma el valor: "PERMITIDA"
Retorno de la función: "[LINUX] Alertas críticas encontradas: 0. Acción: PERMITIDA"


"""
