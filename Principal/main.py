
# Importa las funciones desde app.py
from app import modificar_producto, eliminar_producto, generar_reporte, agregar_producto, ver_producto
import os, sys
# Definición de la lista de productos
productos = [
    {'codigo': '001', 'nombre': 'Producto 1', 'descipcion':'Producto de alta calidad en','stock':'STOK', 'precio': 10.0},
    {'codigo': '002', 'nombre': 'Producto 1', 'descipcion':'Producto de alta calidad en','stock':'STOK', 'precio': 10.0},
    {'codigo': '003', 'nombre': 'Producto 1', 'descipcion':'Producto de alta calidad en','stock':'STOK', 'precio': 10.0},
]

# Ejemplo de uso (agregar esta opción al menú)while True:
while True:
    
    print('''
          \t▀▀█▀▀ █▀▀█ ▀█─█▀   █▀▀▀ █▀▀█ █──█ █▀▀█ █▀▀█   ▀▀▀█ 
          \t──█── █──█ ─█▄█─   █─▀█ █▄▄▀ █──█ █──█ █──█   ──█─ 
          \t ─▀── █▀▀▀ ──▀──   ▀▀▀▀ ▀─▀▀ ─▀▀▀ █▀▀▀ ▀▀▀▀   ─▐▌─''')
    print("\t══════════════════════════════════════════════════════════")
    print(" \tOpciones:")
    print(" \t1 →  [Agregar producto]",end='')
    print("   2 →  [Modificar producto]")
    print(" \t3 →  [Eliminar producto]",end='')
    print("  4 →  [Ver producto]")
    print(" \t5 →  [Generar reporte]",end='')
    print("    0 →  [Salir]\n\t═══════════════════════════════════════════════════════════")
    try:
        opcion = int (input("\tSELECCIONE ITEMS=>:→  "))
        #os.system('cls')
        match opcion:
            case 0:
                print("Saliendo")   
                exit()
            case 1:
                print ("Agregar producto")
                #llamon la funcion agregar producto la misma deve 
                # verificar input y si esta o no  el producto en la lista 
                    #productos = [
                    #    # {
                    #     #    'codigo': '001',
                    #      #   'nombre': 'PAPA',
                    #       #  'descripcion': 'DESCRIPCION',
                    #        3 'stock': 52,
                    #         'precio': 10.0
                    #     },
                    #     {
                    #         'codigo': '002',
                    #         'nombre': 'TORNILLO',
                    #         'descripcion': 'DESCRIPCION',
                    #         'stock': 10, 
                    #         'precio': 15.0
                    #     },
                    # #]
            case 2:
                os.system('cls')
                print ("Modificar producto")
            case 3:
                print ("elimuinar producto")
                codigo = input("Introduce el ID del producto a eliminar: ")
                eliminar_producto(productos, codigo)
            case 4:
                print("Ver Productos")
                codigo = input("Introduce el código del producto a ver: ")
                ver_producto(productos, codigo)
            case 5:
                print("Crear Matriz de Reporte")
                       
            case _:
                print("Opcion no valida ingrese opcion de 0 1 5 por favor ")
    except UnicodeEncodeError : 
        print ("Ingrese un valor valido ")
    except ValueError:
        print("Error de caracter ingrese solo numeros ")
#        os.system('cls')
#        agregar_producto(productos)
#     elif opcion == '2':
#        
#         codigo = input("Introduce el código del producto a modificar: ")
#         modificar_producto(productos, codigo)
#     elif opcion == '3':
#         os.system('cls')
#         print('''
#               █▀▀ █░░ █ █▀▄▀█ █ █▄░█ █▀▀ █▀▄▀█ █▀█ █▀   █▀▀ █░░   █▀█ █▀█ █▀█ █▀▄ █░█ █▀▀ ▀█▀ █▀█   █▀█ █▀█ █▀█   █ █▀▄
#               ██▄ █▄▄ █ █░▀░█ █ █░▀█ ██▄ █░▀░█ █▄█ ▄█   ██▄ █▄▄   █▀▀ █▀▄ █▄█ █▄▀ █▄█ █▄▄ ░█░ █▄█   █▀▀ █▄█ █▀▄   █ █▄▀
#           ''')
#         codigo = input("Introduce el ID del producto a eliminar: ")
#         eliminar_producto(productos, codigo)
#     elif opcion == '4':
#         codigo = input("Introduce el código del producto a ver: ")
#         ver_producto(productos, codigo)
#     elif opcion == '5':
#         generar_reporte(productos)
#     elif opcion == '0':
#         break
#     else:
#         print("Opción no válida. Introduce un número del 1 al 6.")