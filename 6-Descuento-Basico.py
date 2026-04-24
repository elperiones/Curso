# 6 PROGRAMA PARA VERIFICAR DESCUENTOS PORCENTUALES

compra = float(input("Introduce el monto total de la compra: $"))

if compra > 100: 
    descuento = compra * 0.15
    total = compra - descuento
    print(f"¡Felicidades! Tienes un descuento del 15% = ${descuento:.2f}")
else:
    total = compra
    print("No se aplicó descuento (la compra debe ser mayor a $100)")
    
print(f"El total a pagar es: ${total:.2f}")