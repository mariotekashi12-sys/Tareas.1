print("--- BIENVENIDOS A RIVERA COFFEE ---")
print("1. Pedir un American coffee")
print("2. Pedir un Capuchino")
print("3. Pedir un Té Verde")

opcion = input("\nPor favor, selecciona una opción (1-3): ")

if opcion == "1":
    print("☕ ¡Excelente elección! Tu American Coffee intenso está en camino.")
elif opcion == "2":
    print("🥛 Ok muy bien un Capuchino cremoso con mucha espuma.")
elif opcion == "3":
    print("🍃 Aquí tienes tu Té Verde relajante. ¡Disfrútalo!")
else:
    print("❌ Opción no válida. Por favor, elige un número del 1 al 3.")
