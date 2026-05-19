# 1. IMPORTACIÓN
# Importamos la biblioteca externa y le asignamos un alias 'np' para facilitar su uso
import numpy as np
def procesar_estadisticas(lista_mensajes):
    """
    Función que recibe datos y utiliza funciones externas de
    la biblioteca NumPy para procesarlos.
    """
    # Invocación de función externa para el promedio
    promedio = np.mean(lista_mensajes)

    # Invocación de función externa para encontrar el valor máximo
    pico_maximo = np.max(lista_mensajes)

    # Invocación de función externa para la desviación estándar
    desviacion = np.std(lista_mensajes)

    media=np.median(lista_mensajes) #calculo de mediana

    return promedio, pico_maximo, desviacion, media

def main():
        # --- Programa Principal ---
    # Datos: Mensajes enviados cada hora durante un turno de 8 horas
    datos_servidor = [15, 42, 88, 30, 120, 55, 72, 20]
    # Llamada a nuestra función enviando los parámetros de entrada
    prom, maximo, ds, median  = procesar_estadisticas(datos_servidor)
    print("=== REPORTE DE ACTIVIDAD DEL SERVIDOR ===")
    print(f"Promedio de mensajes por hora: {prom:.2f}")
    print(f"Pico de actividad registrado: {maximo} mensajes")
    print(f"Variabilidad del tráfico (Desviación): {np.round(ds, 2)}")
    print(f"calculo de medianas): {median:.2f}")

if __name__=="__main__":
    main()

#si intentas utilizar np.mean() sin haber hecho el import
#al principio del archivo, independientemente de la estructura del código tendrás un 
# error que hará que no funcione.