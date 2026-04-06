N = int(input("Ingresa un número: "))

if N < 0:
    print("No existe el factorial de números negativos")
else:
    factorial = 1
    i = 1

    while i <= N:
        factorial = factorial * i
        i = i + 1

    print("El factorial es:", factorial)


    