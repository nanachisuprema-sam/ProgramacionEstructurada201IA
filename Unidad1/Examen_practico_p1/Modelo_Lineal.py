#Estimación de Activación de Neurona Artificial (Modelo Lineal):

#Diseñar un algoritmo que calcule el valor de Activación (Z) de una neurona simple 
# antes de pasar por su función no lineal. 
# El programa debe solicitar al usuario el valor del "Peso de entrada" (w) y 
# el valor del "Dato de entrada" (x). 
# Aplica el modelo de regresión simple Z = w * x (asumiendo un sesgo/bias de cero).

w=float(input("Ingrese peso de entrada W"))
x=float(input("ingrese por favor el dato de entrada X"))
z= w * x
print("El resultado de Z es: ", z)
