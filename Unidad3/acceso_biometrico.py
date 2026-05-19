Nombre_Ingeniero = input("Por favor, ingrese su nombre: ")
ID_Empleado = int(input("Por favor, ingrese su ID: "))

coso1 = input("¿El escaneo de Iris coincide con la base de datos? (si/no): ").lower()
coso2 = input("¿El reconocimiento facial es mayor al 95%? (si/no): ").lower()

if ID_Empleado < 1:
    print("¡ALERTA DE SEGURIDAD! ID inválido detectado. Bloqueando accesos y notificando a la policía.")

elif coso1 != "si" or coso2 != "si":
    print("Error Biométrico: Identidad no verificada al 100%. Por favor, contacte a seguridad.")

elif ID_Empleado < 100:
    print(f"Bienvenido, Ingeniero {Nombre_Ingeniero}. Acceso nivel SENIOR concedido a todas las áreas.")
    
else:
    print(f"Bienvenido, Ingeniero {Nombre_Ingeniero}. Acceso nivel JUNIOR concedido. Áreas de servidores restringidas.")



