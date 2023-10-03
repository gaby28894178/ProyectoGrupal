
listaProductos = []
terminar = True

while True:
    opcion = int(input("Menú de opciones \n\n Ingrese \n\n (1) Agregar un Nuevo Producto \n (2) Mostrar la lista de Productos \n (3) Salir del Menú \n"))

    if opcion == 1:
        codigo = input("Ingrese un nuevo código: ")
        # Verifica si el código ya existe en la lista
        if codigo in [producto['codigo'] for producto in listaProductos]:
            print("El código ya existe, ingrese otro código.")
        else:
            producto = input("Ingrese el nombre del producto: ")
            precio = float(input("Ingrese el Precio del Producto: $ "))
            descrip = input("Ingrese descripción del producto: ")
            cantidad = int(input("Ingrese la cantidad adquirida: "))
            
            # Agrega el nuevo producto a la lista de productos
            nuevo_producto = {
                'codigo': codigo,
                'producto': producto,
                'precio': precio,
                'descripcion': descrip,
                'cantidad': cantidad
            }
            listaProductos.append(nuevo_producto)
            print("El Producto se ingresó correctamente.\n")

    elif opcion == 2:
        print("Lista de Productos:")
        for producto in listaProductos:
            print(f"Código: {producto['codigo']}\n Producto: {producto['producto']}\n Precio: ${producto['precio']}\n Descripción: {producto['descripcion']}\n Cantidad: {producto['cantidad']}")
            
    elif opcion == 3:
        terminar = False
        print("Usted eligió SALIR.\n")
        break

    else:
        print("Ingresó una opción inválida.")
