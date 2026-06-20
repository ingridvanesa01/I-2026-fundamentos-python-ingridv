import pandas

# Cargar el archivo CSV
datos= pandas.read_csv("clase 08/estudiantes.csv")

#mostrar las primeras filas del DataFrame
print(datos.head(2))

#mostar solo las columnas "Nombre" y "apellido"
print(datos[["nombre", "apellido"]].head(5))

#calcular estadisticas descriptivas
print(datos.describe(3))

#calcular la media de la columna "Edad"
print(datos["edad"].max())

#calcular el minimo de la edad
print(datos["edad"].min())

#filtrar los estudiantes mayor a 85 
estudiantes_alta_nota= datos[datos["nota"] > 85]
print(estudiantes_alta_nota)

 #agrupar por genero y calcular la media de las notas
media_notas_por_genero= datos.groupby("sexo")["nota"].mean()
print(media_notas_por_genero)



