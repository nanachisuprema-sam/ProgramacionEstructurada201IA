UMBRAL_PEQUENO= 5.0 
UMBRAL_GRANDE =20.0 

dimension= float(input("Ingrese tmaño plis"))
if dimension <= 0: 
    print("Error: Lectura inválida. Verifique el sensor.")
elif dimension < 0 or dimension==UMBRAL_PEQUENO:
    print("Clasificación: Micro-componente (Grado A)")
elif dimension < UMBRAL_PEQUENO and dimension<= UMBRAL_GRANDE:
    print("Clasificación: Componente Estándar (Grado B)") 
elif dimension> UMBRAL_GRANDE:
    volumen= dimension* dimension * dimension
    print(f"Clasificación: Componente Industrial (Grado C), volumen del cubo: {volumen}")

print("Registro de inspección completado.")