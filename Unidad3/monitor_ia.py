Temperatura_GPU= float(input("inserta la enperatura de la GPU (grados Celsius)"))
Porcentaje_Memoria_VRAM= int(input("ingresa porcentaje de uso de Memoria VRAM (de 0 a 100)"))
sis= input("el Sistema de Enfriamiento Líquido está activo? (si/no)").lower().strip()
if Temperatura_GPU > 90 and Porcentaje_Memoria_VRAM==100:
    print("CRÍTICO (Apagado Inmediato)")
elif Temperatura_GPU > 75 and sis== "si":
    print( "Temperatura elevada. Reduciendo velocidad de procesamiento (Throttling).")
elif Temperatura_GPU > 75 and sis== "no":
    print("Peligro: Temperatura alta y enfriamiento desactivado. Pausando entrenamiento.")
elif Temperatura_GPU < 75 and Porcentaje_Memoria_VRAM <80:
    print("Sistema Estable: Entrenamiento en curso a máxima capacidad.")
elif Porcentaje_Memoria_VRAM > 100 or Porcentaje_Memoria_VRAM < 0:
    print("Error: Lectura de memoria fuera de rango (0-100%).")