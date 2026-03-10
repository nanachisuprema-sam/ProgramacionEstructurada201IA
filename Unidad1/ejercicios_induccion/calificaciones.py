#sacar calificaciónes (agregar funciones, main, etc)
def calificacion():
    puntos = int(input("por favor, ingresa número de puntos del 1 al 100 "))
    if puntos >90:
        print("La calificación es A")
    elif puntos >80:
        print("Calificación es B")
    elif puntos >70:
        print("su calificación es C")
    elif puntos >60:
        print("su calificación es D")
    else:
        print("su calificación es F")

def main():
    calificacion()

if __name__=="__main__": 
    main()