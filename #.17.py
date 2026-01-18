peso = float(input("Introduce tu peso en kg: "))
altura = float(input("Introduce tu altura en metros: "))

imc = peso / (altura ** 2)

print(f"\nTu IMC es: {imc:.2f}")

if imc < 18.5:
    clasificacion = "Bajo peso"
elif 18.5 <= imc < 25:
    clasificacion = "Peso normal (saludable)"
elif 25 <= imc < 30:
    clasificacion = "Sobrepeso"
else:
    clasificacion = "Obesidad"

print(f"Categoría: {clasificacion}")
