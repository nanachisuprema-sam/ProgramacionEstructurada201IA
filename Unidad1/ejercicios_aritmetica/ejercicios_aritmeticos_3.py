import math
#demostración del uso de funciones math

def mostrar_funciones_math(numero):
    #crear variable

    sen_x=math.sin(numero)
    conse_x=math.cos(numero)

    print("el seno de", numero, "es:", sen_x)
    print("el coseno de", numero, "es:", conse_x)

    resultado= sen_x ** 2 + conse_x ** 2

    print("el resultado de sen^2(x) es:", resultado)

def main():
    numero= float(input("ingrese numero: "))
    mostrar_funciones_math(numero)
if __name__== "__main__":
    main()