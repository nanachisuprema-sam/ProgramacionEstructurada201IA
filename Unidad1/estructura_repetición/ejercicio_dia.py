def diasem():
    print("Dias de la semana")
    dia= input("ingrese un numero del 1-7")

    match dia:
        case "1":
            print("lunes")
        case "2":
            print("martes")
        case "3":
            print("miercoles")
        case "4":
            print("jueves")
        case "5":
            print("viernes")
        case "6":
            print("sabado")
        case "7":
            print("domingo")

def main():
    diasem()

if __name__== "__main__":
    main()