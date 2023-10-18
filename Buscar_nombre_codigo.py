print ("""""""""""""""""""""""""""""""""""""""""""""""""""""")
print ("                  BUSCAR/ CODIGO                    ")                                      
print ("""""""""""""""""""""""""""""""""""""""""""""""""""""")


def ingresarNombre(productos, nombre):
    encontrado = False
    for producto in productos:
        if producto['nombre'].upper() == nombre.upper():
            encontrado = True
            print("Producto encontrado:")
            print(f"Código: {producto['codigo']}")
            print(f"Nombre: {producto['nombre']}")
            print(f"Precio: {producto['precio']}")
            break

    if not encontrado:
        print(f"No se encontró ningún producto con el nombre {nombre}")

def ingresarCodigo(productos, codigo):
    encontrado = False
    for producto in productos: 
        if producto ['codigo'].upper()==codigo.upper():
            encontrado =True
            print("Codigo encontrado")
            print (f"Codigo {producto['codigo']}")
            print (f"Nombre {producto['nombre']}")
            print (f"Precio {producto['precio']}")
            break

    if not encontrado:  
            print(f"Codigo no encontrado{codigo}")  
        
productos = [
    {'codigo': '001', 'nombre': 'PAN', 'descripcion': 'Descripción 1', 'stock':"10", 'precio': 10.0},
    {'codigo': '002', 'nombre': 'LECHE', 'descripcion': 'Descripción 2', 'stock': "5", 'precio': 15.0},
    {'codigo': '003', 'nombre': 'TORNILLO', 'descripcion': 'Descripción 3', 'stock': "8", 'precio': 20.0},
]

while True: 
     
    print ("""
    (1) Buscar por nombre
    (2) Buscar por código
    (0) Salir
    """)

    try:
        
        opcion = int (input("\tSELECCIONE una opción =>: "))
        if opcion == 0:
            print("Saliendo")   
            exit()

        elif opcion == 1:
            print ("Usted quiere buscar por nombre")
            nombre = input("Ingrese el nombre a buscar")
            ingresarNombre(productos, nombre)

        elif opcion == 2:
            print ("Usted quiere buscar por codigo")
            codigo = input ("Ingrese el codigo a buscar")
            ingresarCodigo(productos, codigo)
        else:
            print("Opción no válida, ingrese opción 0, 1, o 2 por favor.")
    except ValueError:
        print("Error de caracter, ingrese solo números o nombres.")
