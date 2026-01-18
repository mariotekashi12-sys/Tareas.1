try:
    precio_original = float(input("Introduce el precio del producto: "))

      if precio_original >= 100:
        descuento = precio_original * 0.15
        precio_final = precio_original - descuento
        print(f"¡Se aplica un descuento del 15%! Ahorras: ${descuento:.2f}")
    else:
        precio_final = precio_original
        print("El precio es menor a $100, no hay descuento disponible.")

    print(f"El precio final a pagar es: ${precio_final:.2f}")

except ValueError:
    print("Error: Por favor, introduce un número válido (ejemplo: 120.50).")

