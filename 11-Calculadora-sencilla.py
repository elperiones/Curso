# 11 PROGRAMA PARA CALCULADORA SENCILLA

numero1 = float(input("Ingrese su primer numero:"))
numero2 = float(input("Ingrese su segundo numero:"))
operador = input("Ingrese su operador (+, -, *, /):")

if operador == "+":
    resultado = numero1 + numero2
    print(f"Resultado: {numero1} + {numero2} = {resultado}")
elif operador == "-":
    resultado = numero1 - numero2
    print(f"Resultado: {numero1} - {numero2} = {resultado}")
elif operador == "*":
    resultado = numero1 * numero2
    print(f"Resultado: {numero1} * {numero2} = {resultado}")
elif operador == "/":
    if numero1 or numero2 != 0:
        resultado = numero1 / numero2
        print(f"Resultado: {numero1} / {numero2} = {resultado}")
    else:
        print("Error: No es posible dividir por cero.")
else:
    print("Error: Operador no valido. Por favor usa +, -, * o /")