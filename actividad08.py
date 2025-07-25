products = []
while True:
    print("------------------CONTROL DE PRODUCTOS------------------\n"
          "1. Agregar un producto\n"
          "2. Modificar un prodcuto existente\n"
          "3. Eliminar un producto\n"
          "4. Ver todos los productos\n"
           "5. Salir")
    option = input("Ingrese la opcion que desea:")
    match option:
        case "1":
            addp = input("Ingrese el producto a la lista: ")
            products.append(addp)
        case "2":
            print("Actual list:", products)
            modp = int(input("Ingrese el indice que desea modificar: "))
            new_value = input("Ingrese el nuevo valor a agregar: ")
            products[modp] = new_value
            print("¡Elemento modificado!")

        case "3":
            print("Actual list: ", products)
            removep = input("Ingrese el producto que desea eliminar: ")
            products.remove(removep)
            print("!Producto eliminado!")
        case "4":
            print("Actual list: ", products)
        case "5":
            print("¡Saliendo del programa!")
            break
        case _:
            print("Ingrese una opcion valida")



