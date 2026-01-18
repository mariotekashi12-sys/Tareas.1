def calcular_envio(zona, peso):
    costo_base = 0
    descuento = 0

    
    if zona.lower() == "nacional":
        
        if peso <= 5:
            costo_base = 10
        elif peso <= 20:
            costo_base = 20
        else:
            costo_base = 35
            
    elif zona.lower() == "internacional":
        if peso <= 5:
            costo_base = 50
        else:
            costo_base = 80
        
        
        if costo_base > 70:
            descuento = costo_base * 0.10
            
    else:
        return "Zona no válida"

    total = costo_base - descuento
    return total, descuento


zona_usuario = "internacional"
peso_usuario = 12
total, ahorro = calcular_envio(zona_usuario, peso_usuario)

print(f"Zona: {zona_usuario.capitalize()}")
print(f"Peso: {peso_usuario}kg")
print(f"Descuento aplicado: ${ahorro}")
print(f"Costo total de envío: ${total}")

