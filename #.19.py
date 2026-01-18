import math

def resolver_cuadratica(a, b, c):
    
    discriminante = b**2 - 4*a*c
    
    print(f"Ecuación: {a}x² + {b}x + {c} = 0")
    print(f"Discriminante: {discriminante}")

    
    if discriminante > 0:
        x1 = (-b + math.sqrt(discriminante)) / (2*a)
        x2 = (-b - math.sqrt(discriminante)) / (2*a)
        print(f"Hay 2 soluciones reales: x1 = {x1}, x2 = {x2}")
        
    elif discriminante == 0:
        x = -b / (2*a)
        print(f"Hay 1 solución real única: x = {x}")
        
    else:
        print("No hay soluciones reales (el resultado es complejo).")


resolver_cuadratica(1, -5, 6)
