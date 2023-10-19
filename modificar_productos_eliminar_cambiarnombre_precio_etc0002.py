# Crear una lista de productos
productos = [
    {'codigo': '001', 'nombre': 'Martillo', 'descripcion': 'DESCRIPCION', 'stock': 10, 'precio': 250.7, 'fecha_llegada': (2023, 10, 19)},
    {'codigo': '002', 'nombre': 'Destornillador', 'descripcion': 'DESCRIPCION', 'stock': 20, 'precio': 145.6, 'fecha_llegada': (2023, 10, 20)},
    {'codigo': '003', 'nombre': 'Sierra', 'descripcion': 'DESCRIPCION', 'stock': 15, 'precio': 359.9, 'fecha_llegada': (2023, 10, 21)},
    {'codigo': '004', 'nombre': 'Clavos', 'descripcion': 'DESCRIPCION', 'stock': 1000, 'precio': 25.7, 'fecha_llegada': (2023, 10, 22)}
]

# Agregar un diccionario para información adicional del producto
info_adicional = {
    'codigo_proveedor': 'PROV001',
    'ubicacion_almacen': 'Estante 1, Pasillo A'
}

# Función para eliminar un producto por su código
def eliminar_producto(codigo):
    try:
        producto = next(producto for producto in productos if producto['codigo'] == codigo)
        productos.remove(producto)
        print(f"Producto con código {codigo} fue eliminado del stock.")
    except StopIteration:
        print(f"No se encontró un producto con el código {codigo} en el stock.")

# Función para modificar el nombre de un producto
def modificar_nombre(codigo, nuevo_nombre):
    try:
        producto = next(producto for producto in productos if producto['codigo'] == codigo)
        producto['nombre'] = nuevo_nombre
        print(f"Nombre del producto con código {codigo} modificado a {nuevo_nombre}.")
    except StopIteration:
        print(f"No se encontró un producto con el código {codigo} en el stock.")

# Función para modificar el precio de un producto
def modificar_precio(codigo, nuevo_precio):
    try:
        producto = next(producto for producto in productos if producto['codigo'] == codigo)
        producto['precio'] = nuevo_precio
        print(f"Precio del producto con código {codigo} modificado a {nuevo_precio}.")
    except StopIteration:
        print(f"No se encontró un producto con el código {codigo} en el stock.")

# Función para mostrar el stock actual
def mostrar_stock():
    print("Stock actual:")
    for producto in productos:
        print(f"Código: {producto['codigo']}, Nombre: {producto['nombre']}, Stock: {producto['stock']}, Precio: {producto['precio']}, Fecha de llegada: {producto['fecha_llegada']}")

    print(f"Información adicional: Código de proveedor: {info_adicional['codigo_proveedor']}, Ubicación en almacén: {info_adicional['ubicacion_almacen']}")

# Función para realizar la acción deseada por el usuario
def realizar_accion(opcion):
    try:
        if opcion == '1':
            codigo_a_eliminar = input("Ingrese el código del producto que desea eliminar: ")
            eliminar_producto(codigo_a_eliminar)
        elif opcion == '2':
            codigo_a_modificar = input("Ingrese el código del producto que desea modificar: ")
            nuevo_nombre = input("Ingrese el nuevo nombre del producto: ")
            modificar_nombre(codigo_a_modificar, nuevo_nombre)
        elif opcion == '3':
            codigo_a_modificar = input("Ingrese el código del producto que desea modificar: ")
            nuevo_precio = float(input("Ingrese el nuevo precio del producto: "))
            modificar_precio(codigo_a_modificar, nuevo_precio)
        elif opcion == '4':
            return False  # Salir del programa
        else:
            print("Opción no válida. Por favor, ingrese un número de acción válido.")
    except ValueError:
        print("Ingrese un valor numérico válido para el precio.")
    return True

while True:
    mostrar_stock()
    print("\n1. Eliminar producto")
    print("2. Modificar nombre de producto")
    print("3. Modificar precio de producto")
    print("4. Salir")
    
    opcion = input("Ingrese el número de la acción que desea realizar: ")

    if not realizar_accion(opcion):
        break

print("Fin del programa.")
