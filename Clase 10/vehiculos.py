class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        
    def mostrar_info(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.año}")

lista_vehiculos = []
cantidad = int(input("¿Cuántos vehículos deseas registrar? "))

for _ in range(cantidad):
    marca = input("Marca: ")
    modelo = input("Modelo: ")
    año = int(input("Año: "))
    nuevo_vehiculo = Vehiculo(marca, modelo, año)
    lista_vehiculos.append(nuevo_vehiculo)

#mostrar la información de todos los vehículos registrados
for i in range(len(lista_vehiculos)):
    print(f"\nInformación del vehículo {i + 1}:")
    lista_vehiculos[i].mostrar_info()


#lista_vehiculos.append(mostrar_info)

















