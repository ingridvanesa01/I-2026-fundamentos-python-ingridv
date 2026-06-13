#mensaje de inicio
print("Bienvenidos a la aplicacion de calculo de IMC")

#preguntas de datos personales
nombre = input("Ingrese su nombre:")
apellido = input("Ingrese su apellido:")
edad = int(input("Ingrese su edad:"))
peso = float(input("Ingrese su peso en kg:"))
altura = float(input("Ingrese su altura en metros:"))

#calculo del IMC
imc = peso / (altura ** 2)
if imc < 18.5:
    rango = "bajo peso"
elif imc < 18.5 and imc < 25:
    rango = "peso normal"
elif imc < 25 and imc < 30:
    rango = "sobrepeso"
else:
    rango = "obesidad"

    #resultado IMC
    print("----RESULTADOS----") 
    print("Nombre:", nombre, apellido)
    print("Edad:", edad)
    print("Su IMC es:", imc)
    print("rango de peso:", rango)
    