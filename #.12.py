nota = float(input("Introduce la nota (0-100): "))

if nota >= 90 and nota <= 100:
    letra = "A"
elif nota >= 80:
    letra = "B"
elif nota >= 70:
    letra = "C"
elif nota >= 60:
    letra = "D"
elif nota >= 0 and nota < 60:
    letra = "F"
else:
    letra = "Nota no válida"

print(f"Tu calificación es: {letra}")
