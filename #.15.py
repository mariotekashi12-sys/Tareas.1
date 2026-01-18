lado1 = float(input("Ingresa la longitud del primer lado: "))
lado2 = float(input("Ingresa la longitud del segundo lado: "))
lado3 = float(input("Ingresa la longitud del tercer lado: "))

if lado1 == lado2 == lado3:
    print("El triángulo es Equilátero.")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("El triángulo es Isósceles.")
else:
    print("El triángulo es Escaleno.")
