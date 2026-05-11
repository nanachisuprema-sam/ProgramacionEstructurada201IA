puntajes_sentimiento= [0,0, 0]

for i in range (1,6):
    print("palabra", {i})
    respuesta=int(input("¿Qué sentimiento detectas? (0: Positivo, 1: Neutral, 2: Negativo):"))
    puntajes_sentimiento [respuesta] += 1

    print(f"\nContenido final del vector: {puntajes_sentimiento}")

valor_maximo = puntajes_sentimiento[0]
posicion_mayor = 0

for posicion in range(1, 3):
    if puntajes_sentimiento[posicion] > valor_maximo:
        valor_maximo = puntajes_sentimiento[posicion]
        posicion_mayor = posicion

if posicion_mayor == 0:
    print("Resultado de IA: La frase es Positiva")
elif posicion_mayor == 1:
    print("Resultado de IA: La frase es Neutral")
elif posicion_mayor == 2:
    print("Resultado de IA: La frase es Negativa")