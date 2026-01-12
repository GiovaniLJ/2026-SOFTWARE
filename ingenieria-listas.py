#Inser sirve para insertar un elemento en una posición específica de la lista
#append sirve para agregar un elemento al final de la lista
#remove sirve para eliminar un elemento específico de la lista
#pop sirve para eliminar un elemento en una posición específica de la lista y devolverlo
#sort sirve para ordenar los elementos de la lista
#reverse sirve para invertir el orden de los elementos de la lista
# del sirve para eliminar un elemento en una posición específica de la lista sin devolverlo
# [0:3] sirve para obtener una sublista desde el índice 0 hasta el índice 2 (el índice 3 no se incluye)
temperaturas = [22.5, 85.0, 19.8, 92.3, 45.1, 88.6, 23.4, 100.2, 15.0]

del  temperaturas[7]  

max_temperatura = max(temperaturas)
min_temperatura = min(temperaturas)


primeros_tres_valores = temperaturas[0:3]
promedio_primeros_tres = sum(primeros_tres_valores) / 3

promedio_total = sum(temperaturas) / len(temperaturas)

activa_alarma = (promedio_primeros_tres > 40) or (promedio_total > 90)

temperaturas.sort()

print("REPORTE")
print(temperaturas)
print(f"Temperatura máxima registrada: {max_temperatura}°C", f"Temperatura mínima registrada: {min_temperatura}°C", sep="\n")
print(f"Promedio de las primeras tres temperaturas: {promedio_primeros_tres}°C")
print(f"Alerta Activada: {activa_alarma}")
#------------------------------------------------------------