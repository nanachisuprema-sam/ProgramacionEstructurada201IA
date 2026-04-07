def acumulacion():
    suma=0
    while suma<500:
        numero=int(input("ingrese numero"))
        suma+=numero
    return suma

def main():
    resultado= acumulacion()
    print("la suma acumulada es:", resultado)

if __name__=="__main__":
    main()