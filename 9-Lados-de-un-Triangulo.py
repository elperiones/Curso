#9 PROGRAMA PARA VERIFICAR LOS LADOS DE UN TRIANGULO Y EL TIPO DE TRIANGULO

lado1 = float(input("Introduce el primer lado: "))
lado2 = float(input("Introduce el segundo lado: "))
lado3 = float(input("Introduce el tercer lado: "))

if lado1 == lado2 == lado3: 
    print("El triángulo es: Equilátero")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:   
    print("El triángulo es: Isósceles")
else:
    print("El triángulo es: Escaleno")