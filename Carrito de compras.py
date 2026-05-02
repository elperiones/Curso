# CARRITO DE COMPRAS

carrito =[]
precios = []
continuar = True

print("\n" + "-"*50)
print("MENU DEL CARRITO".center(50, " "))
print("-"*50)

while continuar:

    print("1. AGREGAR un nuevo producto")
    print("2. MOSTRAR el carrito")
    print("3. ELIMINAR un producto")
    print("4. CALCULAR el monto total")
    print("5. RENUNCIAR / Salir")
    print("-"*50)

    opcion = input("Selecciona una opción (1-5): ")

    if opcion == "1":
        nombre = input("Introduce el nombre del producto: ")
        precio = float(input(f"Precio de {nombre}: "))
        carrito.append(nombre)
        precios.append(precio)
        print(f"{nombre} añadido con exito!")

    elif opcion == "2":
        if len(carrito) == 0:
            print("\n El carrito esta vacio.")
        else:
            print("\n--- Tu Lista de Compras ---")
            total = 0
            for i in range(len(carrito)):
                print(f"{i+1}. {carrito[i]} - ${precios[i]}")
                total += precios[i]

        print(f"TOTAL A PAGAR: ${total}")
        print("---------------------------")

    elif opcion == "3":
        print("Gracias por su compra. Vuelva pronto!")
        continuar = False

    else:
        print("Opcion no valida, intente de nuevo.")