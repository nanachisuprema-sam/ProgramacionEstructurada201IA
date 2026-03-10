def imprimir_identificadores():
#identificaodores validos
    nombre_usuario= "alumno" #inicia con letra y tiene guión bajo
    sensor= "temperatura" #inicia con letra
    _id_interno= 12 #puede contener guión bajo y números

    print("nombre_usuario")
    print("sensor")
    print("_id_interno12")

#nombre correcto en funciones
def calcular_area():
    print("calcula el área...")

def main():
    imprimir_identificadores()
    calcular_area()

if __name__=="__main__":
    main()

