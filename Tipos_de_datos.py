empleado = "Juan Pablo Martinez Jiron"
edad = 18
estatura = 1.75
gerentedehuipix = True

#Cambia de tipo de variable
estatura_float_to_str_variable= str(estatura)
print(estatura_float_to_str_variable)
print(type(estatura_float_to_str_variable))

print(f"Tipo de nombre: {type(empleado)}")
print(f"Tipo de estatura: {type(estatura)}")
print(f"¿Es gerente de Huipix= {gerentedehuipix}")

#Concatenacion de variables en un print
print(empleado,edad,estatura,gerentedehuipix)
print(f"Los años que tiene el joven es: {edad} años")

#Variables en una sola linea
numero, decimal, nombre = 18, 3.2, "ArtoriasV"
print(numero)
print(f"Hola me llamo Giovani, tengo {numero} años y tomo diario {decimal} litros de agua, mi usarname de videojuegos es {nombre}")

#Tipos de datos
print(type("Por el emperador"))# Tipo str
print(type(5)) # Tipo Int
print(type(1.45)) #Tipo Float
print(type(3 + 1j)) #Tipo complex
print(type(True)) #Tipo bool

#Contador de letras -len()- Empleado 25 letras
print(len(empleado))

#Uso de imput
nombre_usuario = input("Ingresa tu nombre: ")
año_usuario = input("Ingresa tu año de nacimiento: ")
print(f"Hola {nombre_usuario}, tu año de nacimiento es: {año_usuario}")


