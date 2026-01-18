caracter = input("Introduce una letra: ")

caracter = caracter.lower()

if len(caracter) != 1 or not caracter.isalpha():
    print("Por favor, introduce solo una letra del alfabeto.")
elif caracter in 'aeiou':
    print(f"La letra '{caracter}' es una VOCAL.")
else:
    print(f"La letra '{caracter}' es una CONSONANTE.")
