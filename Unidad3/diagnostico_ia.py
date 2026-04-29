import math
from datetime import datetime

now = datetime.now()
print("Sistema de Salud Inteligente -", now)

def calcular_imc(peso, estatura):
    imc = peso / (estatura ** 2)
    return imc

def evaluar_presion(presion_sistolica):
    if presion_sistolica > 140:
        return "Alta"
    else:
        return "Normal"

p = float(input("Ingresa peso (kg): "))
e = float(input("Ingresa estatura (metros, ej: 1.70): "))
presion= int(input("Ingrese presión sistólica: "))

resultado_imc = calcular_imc(p, e)
resultado_presion = evaluar_presion(presion)

imc_final = math.ceil(resultado_imc)

print(f"\nResultado IMC: {imc_final}")
print(f"Estado de Presión: {resultado_presion}")
