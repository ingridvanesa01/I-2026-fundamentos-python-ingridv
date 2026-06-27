class mascota:
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Especie: {self.especie}")
        print(f"Edad: {self.edad}")

#lista para guardar abjetos
mascotas = []

#solicitar cantidad de mascotas 
cantidad = int(input("¿Cuántas mascotas deseas registrar? "))

#registar mascotas

for i in range(cantidad):
    print(f"\nRegistro de mascota {i + 1}:")
    nombre = input("Nombre: ")
    especie = input("Especie: ")
    edad = int(input("Edad: "))

    mascota_obj = mascota(nombre, especie, edad)
    mascotas.append(mascota_obj)

#mostrar informacion de mascotas
for i in range(len(mascotas)):
    print(f"\nInformación de la mascota {i + 1}:")
    mascotas[i].mostrar_info()
    
    


