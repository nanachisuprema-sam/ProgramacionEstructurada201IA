#limpieza de datos, normalización

UMBRAL_ALTO=0.7
UMBRAL_BAJO=0.3

def clasificar_pixeles():
    #solicita al wey del usuaio sus datos
    intensidad= float(input("ingrese intencidad del pixel (0.0 a 0.1): "))
    #si la intencidad es menor a mayor
    if intensidad < 0.0 or intensidad > 1.0:
        print("error: valor de pixel invalido")
        return
    if 0.0 <= intensidad <= UMBRAL_BAJO:
        print(" Clasificación (fondo oscuro)")
        return
    if UMBRAL_BAJO < intensidad < UMBRAL_ALTO:
        print("clasificación (fondo gris)")
        return
    if intensidad >= UMBRAL_ALTO:
        print("clasificación (objeto brillante)")
        return
    print("analisis de imagen fnalizado")

def main():
    clasificar_pixeles()
if __name__=="__main__":
    main()