#importar libreria de Faker:
from faker import Faker


faker= Faker("es_MX")
print("generando datos Dummy con Faker")

print(f"nombre:{faker.name()}")
print(f"dirección:{faker.address()}")
print(f"telefonos:{faker.phone_number()}")
print(f"correo:{faker.email()}")
