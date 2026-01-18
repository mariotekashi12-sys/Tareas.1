print("--- Piedra, Papel o Tijera ---")
jugador1 = input("Jugador 1, elige (piedra, papel, tijera): ").lower()
jugador2 = input("Jugador 2, elige (piedra, papel, tijera): ").lower()

if jugador1 == jugador2:
    print("¡Es un empate!")
else:
    if jugador1 == "piedra":
        if jugador2 == "tijera":
            print("Jugador 1 gana: Piedra aplasta tijera.")
        else:
            print("Jugador 2 gana: Papel envuelve piedra.")
            
    elif jugador1 == "papel":
        if jugador2 == "piedra":
            print("Jugador 1 gana: Papel envuelve piedra.")
        else:
            print("Jugador 2 gana: Tijera corta papel.")
            
    elif jugador1 == "tijera":
        if jugador2 == "papel":
            print("Jugador 1 gana: Tijera corta papel.")
        else:
            print("Jugador 2 gana: Piedra aplasta tijera.")
    else:
        print("Opción no válida. Por favor, escribe piedra, papel o tijera.")
