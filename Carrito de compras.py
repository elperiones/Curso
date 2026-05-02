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
        print(f"{nombre} añadido con exito! \n")

    elif opcion == "2":
        total = 0
        if len(carrito) == 0:
            print("\n El carrito esta vacio. \n")
        else:
            print("\n--- Tu Lista de Compras ---")
            for i in range(len(carrito)):
                print(f"{i+1}. {carrito[i]} - ${precios[i]}")
                total += precios[i]
                print(f"TOTAL A PAGAR: ${total} \n")
                print("---------------------------")

    elif opcion == "3":
        if len(carrito) == 0:
            print("\n No hay nada que eliminar \n")
        else:
            for i in range(len(carrito)):
                print(f"{i+1}. {carrito[i]}")
            
            indice = int(input("Introduce el número del producto a eliminar: ")) - 1
            
            if 0 <= indice < len(carrito):
                eliminado = carrito.pop(indice)
                precios.pop(indice)
                print(f"Has eliminado: {eliminado} \n")
            else:
                print("Número no válido.")

    elif opcion == "4":
        total = sum(precios)
        print(f"\n EL MONTO TOTAL ES: ${total} \n")

    elif opcion == "5":
        print("Gracias por su compra. ¡Vuelva pronto!")
        continuar = False

    else:
        print("Opción no válida, intente de nuevo.")