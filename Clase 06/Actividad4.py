contador = 0
while True:
    #registro de estudiantes
    print("Bienvenidos al registro de estudiantes")
    Nombre = input("ingrse su nombre:")
    Carnet = input ("ingrese su carnet:")
    Nota =float( input("ingrese su nota final:"))
    archivo = open("Clase 06\estudiantes.txt", "a")
    archivo.write(f"Nombre:  {Nombre}\n")
    archivo.write(f"Carnet: {Carnet}\n")
    archivo.write(f"Nota final: {Nota}\n")
    archivo.close()
    
    cntinuar = input("¿Desea registrar otro estudiante? (si/no): ")
    if continuar.lower() == "no":
        break 


