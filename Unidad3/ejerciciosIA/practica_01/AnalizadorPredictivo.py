import os

def limpiar_dato(lectura_cruda):
    try:
        valor = float(lectura_cruda)
        if valor < 0 or valor > 100:
            return None
        return valor
    except ValueError:
        return None

def obtener_estadisticas(lista_datos):
    if not lista_datos:
        return (0, 0, 0)
    maximo = max(lista_datos)
    minimo = min(lista_datos)
    promedio = sum(lista_datos) / len(lista_datos)
    return (maximo, minimo, promedio)

def generar_reporte(total_datos, validos, estadisticas):
    v_max, v_min, v_prom = estadisticas 
    descartados = total_datos - validos
    print("*" * 30)
    print("REPORTE DE ANALISIS PREDICTIVO")
    print("*" * 30)
    print(f"Total de lecturas procesadas: {total_datos}")
    print(f"Lecturas validas: {validos}")
    print(f"Lecturas descartadas: {descartados}")
    print(f"Valor maximo (norm): {v_max:.2f}")
    print(f"Valor minimo (norm): {v_min:.2f}")
    print(f"Valor promedio (norm): {v_prom:.2f}")
    print("*" * 30)

def ejecutar_pipeline():
    datos_finales = []
    cuenta_total = 0
    
    # Manejo de rutas
    ruta_script = os.path.dirname(os.path.abspath(__file__))
    ruta_archivo = os.path.join(ruta_script, "lecturas_sensores.txt")

    if not os.path.exists(ruta_archivo):
        print(f"Error: El archivo {ruta_archivo} no existe.")
        return

    with open(ruta_archivo, "r") as f:
        for linea in f:
            cuenta_total += 1
            valor = limpiar_dato(linea.strip())
            if valor is not None:
                datos_finales.append(valor / 100)

    if datos_finales:
        stats = obtener_estadisticas(datos_finales)
        generar_reporte(cuenta_total, len(datos_finales), stats)
    else:
        print("No se encontraron datos válidos para procesar.")

if __name__ == "__main__":
    ejecutar_pipeline()
