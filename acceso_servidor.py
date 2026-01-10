probabilidad_deteccion = 0.83
temperatura_gpu = 82
uso_memoria_ram = 92.5


activar_alerta = (probabilidad_deteccion > 0.85) and (temperatura_gpu <= 80 or not(uso_memoria_ram > 95))


peso_decision = probabilidad_deteccion ** 2
bloques_ram = (uso_memoria_ram * 32 / 100) // 8

print(f"¿Alerta activada?: {activar_alerta}")
print(f"Peso del modelo: {peso_decision:.4f}")
print(f"Bloques de 8GB ocupados: {bloques_ram}")

#------------------------------------------------------------
#----Acceso a servidor----
tiene_llave_fisica = True
codigo_seguridad = 4512
escaneo_facial_score = 0.88
es_administrador = False

acceso_concedido = (tiene_llave_fisica and (codigo_seguridad == 4512 and (escaneo_facial_score >= .90 or es_administrador))) 
print(f"¿Acceso concedido al servidor?: {acceso_concedido}")