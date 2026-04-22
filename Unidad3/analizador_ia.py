# analizador_ia.py

def normalizar_mensaje(texto):
    return texto.lower().strip()

def detectar_intencion(mensaje_limpio):
    comandos = ["encender", "activar", "reproducir"]
    soporte = ["ayuda", "error", "fallo"]

    if any(palabra in mensaje_limpio for palabra in comandos):
        return "COMANDO DE ACCIÓN"
    elif any(palabra in mensaje_limpio for palabra in soporte):
        return "REPORTE DE SOPORTE"
    else:
        return "CONSULTA GENERAL"

def ejecutar_analizador():
    entrada_usuario = input("Ingrese un comando de voz: ")

    mensaje_procesado = normalizar_mensaje(entrada_usuario)
    categoria = detectar_intencion(mensaje_procesado)
    longitud = len(entrada_usuario)
    
    print("\n--- Resumen del Análisis ---")
    print(f"Mensaje procesado: {mensaje_procesado}")
    print(f"Categoría detectada: {categoria}")
    print(f"Longitud del comando original: {longitud} caracteres")

if __name__ == "__main__":
    ejecutar_analizador()
