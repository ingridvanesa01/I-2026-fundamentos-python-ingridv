print("cajero automatico")
print("Bienvenidos al cajero automatico")
saldo = 0

while True:
    print("1. consultar saldo")
    print("2. retirar dinero")
    print("3. depositar dinero")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print(f"Su saldo actual es: {saldo}")
        saldo += monto
        print(f"Depósito exitoso. Saldo actual: {saldo}")
    elif opcion == 1:
        print(f"Su saldo actual es: saldo")
    elif opcion == "2":
        cantidad = int(input("Ingrese la cantidad a retirar: "))
        if cantidad > saldo:
            print("no suficiente saldo")
        else:
            saldo -= cantidad
            print(f"Ha retirado {cantidad}. Saldo actual: {saldo}")
    elif opcion == "3":
        cantidad = int(input("Ingrese la cantidad a depositar: "))
        saldo += cantidad
        print(f"Ha depositado {cantidad}. Saldo actual: {saldo}")
    elif opcion == "4":
        print("Gracias por usar el cajero automático. ¡Hasta luego!")
        break
    else:
        print ("Opción no válida")
