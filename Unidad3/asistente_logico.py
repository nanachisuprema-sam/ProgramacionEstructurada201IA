import datetime #jiji pa la hora
nombre_asistente= "Susana"

frase = input("Hola! Mi nombre es Susana...¿En qué puedo ayudarte hoy?").lower()
if "hola" in frase or "buenos días" in frase:
    print("¡Holiii! Es un gusto saludarte.")
elif "clima" in frase or "dime el clima" in frase:
    print("El día está oscuro como mi alma, ponte sueter")
elif "hora" in frase or "dime la hora" in frase:
    hoa= datetime.datetime.now().strftime("%H:%M:%S")
    print(f"La hora es: {hoa}")
else:
    print("No te entiendo.")

print("Espero haberte ayudadoooo!")
print("-Susana la del barrio")
