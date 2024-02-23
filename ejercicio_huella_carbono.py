"""
    Calcula la huella de carbono de un individuo en función de su consumo de electricidad y modo de transporte.

    Args:
    consumo_electricidad (float): El consumo mensual de electricidad en kilovatios-hora (kWh).
    modo_transporte (str): El modo de transporte utilizado, que puede ser "coche", "bicicleta" o "transporte público".
    distancia_viaje (float): La distancia total recorrida en kilómetros.

    Returns:
    float: La huella de carbono total en kilogramos de CO2.
"""

def calcular_huella_carbono(consumo_electricidad, modo_transporte, distancia_viaje):
    huella_electricidad = consumo_electricidad * 0.5
    huella_transporte = 0
    
    if modo_transporte == "coche":
        huella_transporte = distancia_viaje * 0.2
    elif modo_transporte == "bicicleta":
        huella_transporte = 0
    elif modo_transporte == "transporte público":
        huella_transporte = distancia_viaje = 0.05
    else:
        return "Modo de trasnporte no válido"
    
    huella_total = huella_electricidad + huella_transporte

    return huella_total




huella_javier = calcular_huella_carbono(250, "coche", 50)
print("La huella de carbono total es: ", huella_javier, "kg CO2")