#10 PROGRAMA PARA VERIFICAR ENTRE 3 NUMEROS CUAL ES EL MAYOR

numero1 = float(input("Ingrese su primer valor:"))
numero2 = float(input("Ingrese su segundo valor:"))
numero3 = float(input("Ingrese su tercer valor:"))

if numero1 >= numero2 and numero1 >= numero3:
    mayor = numero1
elif numero2 >= numero1 and numero2 >= numero3:
    mayor = numero2
else:
    mayor = numero3

print(f"El numero mayor es: {mayor}")