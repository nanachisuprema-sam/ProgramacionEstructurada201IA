intentos = 0
clave_correcta = "gataguapa"
while intentos < 3:

    contrasena = input("Ingrese su contraseña: ")
    if contrasena == clave_correcta:
        print("Acceso Concedido")
        break  
    else:
        intentos += 1
        print(f"Contraseña incorrecta. Intento {intentos} de 3.")
if intentos == 3:
    print("Cuenta bloqueada")
