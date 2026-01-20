lista_obstaculos = ["muro", "caja", "charco"]
bateria_actual = input("Ingrese el nivel de batería actual: ")
distancia_objetivo = 15.5

puede_avanzar = (len(lista_obstaculos) == 3) and (int(bateria_actual) > 20 and distancia_objetivo <= 20)

lista_obstaculos.append("Humano")

print(f"¿El robot puede avanzar?: {puede_avanzar}")

print("TOTAL DE OBSTACULOS:", len(lista_obstaculos))