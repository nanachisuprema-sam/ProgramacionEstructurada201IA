from faker import Faker
fake= Faker ('es_MX')

#declaración de un vetor vacio
ciudades_ia= []

#operación de llenado... ciclo pos
for _ in range(5):
    ciudades_ia.append(fake.city())

#mostrar resultadosss
print("\n--- DATASET DE CIUDADES GENERADO ---")
for i in range(len(ciudades_ia)):
    print(f"Registro {i+1}: {ciudades_ia[i]}")