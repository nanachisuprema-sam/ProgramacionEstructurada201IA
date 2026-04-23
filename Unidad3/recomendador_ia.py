accion = ["Mad Max", "John Wick", "Inception"]
comedia = ["Toy Story", "Minions", "Free Guy"]
terror = ["It", "The Conjuring", "Saw"]

def obtener_recomendación():
    edad=int(input("ingrese su edad"))
    if edad>=13:
        print("por favor, escoja su peicula marcando el número jiji")
        eleccion=int(input("(1)terror, (2)accion, (3)comedia"))
        if eleccion==1:
            print(terror)
        elif eleccion==2:
            print(accion)
        elif eleccion==3:
            print(comedia)
    elif edad < 13:
        print("por favor, escoja su peicula marcando el número jiji")
        eleccion=int(input("(1)terror, (2)accion, (3)comedia"))
        if eleccion==1:
            print("Nota: Debido a tu edad, hemos ajustado la recomendación a contenido apto para todo público.")
        elif eleccion==2:
            print(accion)
        elif eleccion==3:
            print(comedia)

if __name__=="__main__":
   obtener_recomendación()