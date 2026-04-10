import math
def calculo_identidad():
    x=42
    numero_radianes= math.radians(x)
    seno_x=math.sin(numero_radianes)**2
    coseno_x=math.cos(numero_radianes)**2
    identidad= seno_x - coseno_x

    print(f"para x= {x} grados: (sin x)2 + (cos x)2 = {identidad}")
def main():
    x=int(input("ingrese el valor de x en grados: "))
    calculo_identidad()

if __name__=="__main__":
    main()