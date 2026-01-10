#Uso de operadores con input y condiciones, se usa para preguntar cosas y respecto a sus respuestas dar un resultado si o no

consolas = input("Cuantas consolas tienes?")
juegos = input("Cuantos juegos tienes?")

aplicacas_en_conocimiento = int(consolas) >= 3 and int(juegos) >=11

mensaje = f"Aplicas para el puesto por tu conocimiento en consolas" if aplicacas_en_conocimiento else f"No aplicas para el puesto por tu poco conocimiento en consolas"
print(mensaje)

print("Gracias por aplicar, Lindo dia")

#------------------------------------------------------------

edad= input("Cual es tu edad?")
calificacion= input("Cual es tu calificacion en el ultimo semestre?")

aplicas_para_beca = int(edad) >=18 and float(calificacion) >8.5

mensaje_beca = f"Aplicas para la beca Universitaria Benito Juarez, Felicidades!" if aplicas_para_beca else f"No aplcias para beca, sigue enforzandote, animo"
print(mensaje_beca)

print("Gracias por participar, Exito en tu vida academica")

#----Aqui necesitas declarar la variable donde pregunte cuantos años? en int o en float para que pueda restar y dar el resultado correcto----
edad = 25
años_faltates = edad - int(input("Cual es tu edad actual?"))
print(f"Faltan {años_faltates} años para que tengas 25 años")
#------------------------------------------------------------

#----Operadores Aritmeticos
print(3 + 4) #Suma
print(10 - 2) #Resta
print(5 * 6) #Multiplicacion
print(8 / 2) #Division
print(7 % 3) #Modulo, te da el residuo
print(2 ** 3) #Exponente
print(15 // 2) #Division entera, te da el numero entero sin decimales
#---Operadores de comparacion----
print(4 == 4) #Igual que
print(5 > 3) #Mayor que
print(2 < 6) #Menor que
print(7 >= 7) #Mayor o igual que
print(3 <= 5) #Menor o igual que
print(4 != 5) #Diferente que
#---Operadores logicos----
print(True and False) #AND
print(True or False) #OR
print(not True) #NOT
#------------------------------------------------------------
#----Operadores de asignacion----
x = 10
x += 5  # Equivalente a x = x + 5
print(x)
x -= 3  # Equivalente a x = x - 3
print(x)
x *= 2  # Equivalente a x = x * 2
#---Y asi sucesivamente con /=, %=, **=, //=
#------------------------------------------------------------

probabilidad_deteccion = 0.87
temperatura_gpu = 82
uso_memoria_ram = 92.5

