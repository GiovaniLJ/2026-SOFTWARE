equipos = [
    {"nombre": "Nodo-01", "gpu": "RTX 5070 Ti", "vram_uso": 12, "status": "activo", "hashrate": 120.5},
    {"nombre": "Nodo-02", "gpu": "RTX 4090", "vram_uso": 22, "status": "activo", "hashrate": 200.0},
    {"nombre": "Nodo-03", "gpu": "RTX 5070 Ti", "vram_uso": 4, "status": "mantenimiento", "hashrate": 0.0},
    {"nombre": "Nodo-04", "gpu": "A100", "vram_uso": 75, "status": "activo", "hashrate": 450.2},
    {"nombre": "Nodo-05", "gpu": "RTX 5070 Ti", "vram_uso": 15, "status": "activo", "hashrate": 118.0},
    {"nombre": "Nodo-06", "gpu": "RTX 3060", "vram_uso": 10, "status": "error", "hashrate": 0.0}
]

activos = []
inactivos = []
mis_5070 = []
total_hashrate = 0.0

print("USO DE VRAM Y ESTADO DE EQUIPOS")

for equipo in equipos:
    vram = equipo["vram_uso"]
    
    if vram > 20:
        print(f"{equipo['nombre']}, -CRITICO: Memoria Casi Llena ")
    else:
        print(f"{equipo['nombre']}, -OK: Memoria en Nivel Seguro ")

    if equipo["status"] == "activo":
        activos.append(equipo["nombre"])

    if equipo["status"] == "mantenimientos" or equipo["status"] == "error":
        inactivos.append(equipo["nombre"])

    if equipo["gpu"]== "RTX 5070 Ti":
        mis_5070.append(equipo["nombre"])
        
    if equipo["hashrate"]:
        total_hashrate += equipo["hashrate"]
    
print("\n--- REPORTE FINAL ---")
print(f"Equipos Activos: {len(activos)} - {activos}")
print(f"Equipos Inactivos: {len(inactivos)} - {inactivos}")
print(f"Equipos con RTX 5070 Ti: {len(mis_5070)} - {mis_5070}")

print(f"Hashrate Total de la Granja: {total_hashrate} MH/s")
precio_hashrate = float(input("\nIngrese el precio por unidad de hashrate: "))

ganancia_total = total_hashrate * precio_hashrate

print(f"Ganancia Total Estimada: ${ganancia_total:.2f}")
