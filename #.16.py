a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))
c = float(input("Ingresa el tercer número: "))

if a >= b and a >= c:
    mayor = a
elif b >= a and b >= c:
    mayor = b
else:
    mayor = c

print(f"El número más grande es: {mayor}")
