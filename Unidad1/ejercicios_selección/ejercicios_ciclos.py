#lol
def ejemplo_for():
    print("estructura for")

    frutas= {"manzana", "banana", "naranja"}
    #for para itear listas
    for fruta in frutas:
        print(fruta)
        #for para itear rango
    for i in range(1,5):
        print(i)
    #for para itear rangos con paso
    for i in range(1,10,2):
        print(i)

#ejemplo while
def ejemplo_while():
    print("estructura while")
    contador=0

    while contador < 5:
        print(contador)
        contador +=1

#simulación de do while

def ejemplo_do_while():
    print("estructura Do while")

    secreto= "python12"
    intentos=0

    while True:
        intentos_usuario="python12" #simulamos entrada e usuario
        intentos +=1

        if intentos_usuario == secreto:
            print("acceso concedido!")
            break
        else:
            print("acceso denegado, intentar de nuevo")
            break
        print("\n")
