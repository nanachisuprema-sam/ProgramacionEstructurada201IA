#tabla de multi lol
#end="/t" (fila 7 por las dudas)
print("tablita de multiplicar 4 por al 15 quecarajos")
# i columnaj filaaaa wakaka
for i in range(1,15):
    for j in range(1,15):
        print(i *j)
print

print("  ", end="")
for j in range(1, 16):
    print(f"{j:4}", end="")
print()

# Tabla
for i in range(1, 16):
    print(f"{i:2}", end="")  # número de la fila
    for j in range(1, 16):
        print(f"{i*j:4}", end="")
    print()