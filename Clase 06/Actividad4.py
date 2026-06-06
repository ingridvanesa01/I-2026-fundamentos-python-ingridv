print("Bienvenidos al registro de estudiantes")
Nombre = input("ingrse su nombre:")
Carnet = input ("ingrese su carnet:")
Nota =float( input("ingrese su nota final:"))

Archivo = open("Clase 06\estudiantes.txt", "a")
Archivo.write(f"Nombre:  {Nombre}\n")
Archivo.write(f"Carnet: {Carnet}\n")
Archivo.write(f"Nota final: {Nota}\n")
Archivo.close()


