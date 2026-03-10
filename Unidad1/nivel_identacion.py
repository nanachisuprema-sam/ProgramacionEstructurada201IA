#ejemplo para visualizar la identificación en python

def explicar_identificacion():
    #nivel 1
    mensaje= "nivel 1 de identación"
    print(mensaje)

    puntos=10

    if puntos >9:
        #nivel2
        print("entra al flujo de if")

        if puntos ==10:
            #nivel3
            print("puntos igual 10")

    #cierra nivel 1

def main():
    explicar_identificacion()

if __name__=="__main__": 
    main()
