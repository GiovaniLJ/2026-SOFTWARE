# 1. Tu arsenal tecnológico
mi_hardware = ["Ryzen 7 9700X", "RTX 5070 Ti", "32GB DDR5"]

# 2. Agregar un elemento nuevo (Lo que planeas comprar o aprender)
mi_hardware.append("Monitor 4K")

# 3. Insertar algo en una posición específica (en la posición 1, o sea, segundo lugar)
mi_hardware.insert(1, "WSL2 Linux")

# 4. El desafío de hoy: ¿Cómo accederías al ÚLTIMO elemento sin saber cuántos hay?
# Pista: Python permite índices negativos.
ultimo = mi_hardware[-1]

print(f"Mi setup completo: {mi_hardware}")
print(f"Lo último que agregué fue: {ultimo}")

# 5. Ordenar la lista (Útil para organizar datos de mayor a menor)
mi_hardware.sort()
print(f"Hardware ordenado alfabéticamente: {mi_hardware}")

# Suponiendo que tu lista es: ["Ryzen", "WSL2", "RTX 5070 Ti", "DDR5"]

elemento_extraido = mi_hardware.pop(2) 

print(f"Extraje la tarjeta: {elemento_extraido}")
print(f"Así quedó la lista ahora: {mi_hardware}") 
# ¡Verás que la RTX 5070 Ti ya no está!

