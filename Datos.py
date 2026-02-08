servidores = [
    {"id": "Srv-A1", "modelo": "RTX 5070 Ti", "temp": 45.0, "carga": 80, "online": True},
    {"id": "Srv-A2", "modelo": "RTX 5070 Ti", "temp": 82.5, "carga": 95, "online": True},
    {"id": "Srv-B1", "modelo": "A100 Tensor Core", "temp": 35.2, "carga": 10, "online": False},
    {"id": "Srv-B2", "modelo": "RTX 5070 Ti", "temp": 95.0, "carga": 100, "online": True},
    {"id": "Srv-C1", "modelo": "H100 Hopper", "temp": 50.0, "carga": 60, "online": True}
]

# 1. Preparamos nuestras variables vacías (Acumuladores)
modelos_rtx = []
carga_total_online = 0

print("--- MONITOREO DE TEMPERATURAS ---")
for servidor in servidores:
    temp = servidor["temp"]
    
    # Lógica de alertas
    if temp > 90:
        print(f"ALERTA CRÍTICA: {servidor['id']} ({servidor['modelo']}) APAGADO EMERGENCIA - {temp}°C")
    elif temp > 80:
        print(f"ADVERTENCIA: {servidor['id']} ({servidor['modelo']}) SOBRECALENTAMIENTO - {temp}°C")
    else:
        print(f"OK: {servidor['id']} operando normal a {temp}°C")

    # 2. INVENTARIO AUTOMÁTICO: Si es 5070 Ti, la guardamos
    if servidor["modelo"] == "RTX 5070 Ti":
        modelos_rtx.append(servidor["id"])

    # 3. SUMA DE CARGA: Si está online, sumamos su carga
    if servidor["online"]:
        carga_total_online += servidor["carga"] # Esto es igual a: carga = carga + nuevo_valor

# --- FUERA DEL BUCLE (EL REPORTE FINAL) ---
print("\n--- REPORTE TÉCNICO ---")
print(f"Modelos RTX detectados: {len(modelos_rtx)}")
print(f"Carga total del sistema: {carga_total_online}%")

# Pedimos el precio una sola vez
precio_luz = float(input("\nIngrese el precio de la luz por unidad de carga: "))
pago_total = carga_total_online * precio_luz

print(f"El costo operativo total es de: ${pago_total:.2f}")
