UMBRAL_ALTO = 80.0 
UMBRAL_MINIMO = 40.0 
ins= input("ingresa instrucción...")
print("Instrucción recibida! realizando...:", ins)
C=float(input("Por favor ingresa el nivel de confianza"))
if C > UMBRAL_ALTO:
    print(f"Ejecutando la acción: {ins}... (Éxito)", C)
    if C > 95.5:
        print("Aviso: El modelo ha sido reforzado con éxito debido a la alta confianza.")
elif C >= UMBRAL_MINIMO:
    print(f"Confianza insuficiente. ¿Se refiere a: {ins}? Por favor confirme.")
else:
    print("Error 404: No pude entender la instrucción. Intente hablar más claro.")
print("Sesión de procesamiento finalizada.")