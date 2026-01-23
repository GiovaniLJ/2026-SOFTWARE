jugadores = [
    {"tag": "Pro_Giovani", "nivel": 85, "consola": "PC"},
    {"tag": "Noob_Master", "nivel": 10, "consola": "Xbox"},
    {"tag": "Pro_Hunter", "nivel": 92, "consola": "PS5"},
    {"tag": "Ghost_Sniper", "nivel": 45, "consola": "PC"}
]

conteo_admitidos = 0

# 1. Iniciamos el bucle para revisar cada expediente
for jugador in jugadores:
    
    # 2. Extraemos los datos que nos interesan del jugador actual
    nombre = jugador["tag"]
    puntos = jugador["nivel"]
    
    # 3. 
    # Aplicamos el filtro (Aquí es donde usas lo que aprendiste de 'if' y 'and')
    # Queremos que el nombre empiece con "Pro_" Y que los puntos sean >= 80
    if nombre.startswith("Pro_") and puntos >= 80:
        print(f"Jugador {nombre} ADMITIDO ✅")
        # 4. Si entra, lo sumamos al contador
        conteo_admitidos = conteo_admitidos + 1
    else:
        print(f"Jugador {nombre} RECHAZADO ❌")

# 5. Al final (fuera del for), mostramos el resultado total
print(f"\nTotal de nuevos reclutas: {conteo_admitidos}")

lote_gpus = [
    {"serie": "TX-100", "vram": 16, "encendida": True},
    {"serie": "TX-101", "vram": 8, "encendida": True},
    {"serie": "TX-102", "vram": 16, "encendida": False},
    {"serie": "TX-103", "vram": 16, "encendida": True}
]

tarjetas_admitidas = 0

for gpu in lote_gpus: 
    
    name = gpu["serie"]
    memoria = gpu["vram"]
    estado = gpu["encendida"]

    if memoria == 16 and estado == True:
        print(f"GPU LISTAS PARA SALIR {name}")
        tarjetas_admitidas = tarjetas_admitidas + 1
    else:
        print(f"GPU NO APTA {name}")

    print("---- TOTAL DE GPUS ACEPTASDAS ----")
    print(f"\nTotal de GPUs aceptadas: {tarjetas_admitidas}")
    