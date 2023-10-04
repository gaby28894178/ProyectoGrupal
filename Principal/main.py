
# Importa las funciones desde app.py
#from app import modificar_producto, eliminar_producto, generar_reporte, agregar_producto, ver_producto
# Aca cada cual deve de  colocar la carpeta q importa con su funcion
# ejemplo funcion agregar o eliminar ect 




import os, sys
# Definición de la lista de productos
productos = [
    {'codigo': '001', 'nombre': 'Producto 1', 'descipcion':'Producto de alta calidad en','stock':'STOK', 'precio': 10.0},
    {'codigo': '002', 'nombre': 'Producto 1', 'descipcion':'Producto de alta calidad en','stock':'STOK', 'precio': 10.0},
    {'codigo': '003', 'nombre': 'Producto 1', 'descipcion':'Producto de alta calidad en','stock':'STOK', 'precio': 10.0},
]
def mostrarMenu():
    print('''
          \t▀▀█▀▀ █▀▀█ ▀█─█▀   █▀▀▀ █▀▀█ █──█ █▀▀█ █▀▀█   ▀▀▀█ 
          \t──█── █──█ ─█▄█─   █─▀█ █▄▄▀ █──█ █──█ █──█   ──█─ 
          \t ─▀── █▀▀▀ ──▀──   ▀▀▀▀ ▀─▀▀ ─▀▀▀ █▀▀▀ ▀▀▀▀   ─▐▌─''')
    print("\t══════════════════════════════════════════════════════════")
    print(" \t⏺\t⏺\t⏺\t⏺\t Opciones:  [(⊙_⊙;)]  ")
    print(" \t1 →  [Agregar producto]",end='')
    print("   2 →  [Modificar producto]")
    print(" \t3 →  [Eliminar producto]",end='')
    print("  4 →  [Ver producto]")
    print(" \t5 →  [Generar reporte]",end='')
    print("    0 →  [Salir]\n\t═══════════════════════════════════════════════════════════")

# Ejemplo de uso (agregar esta opción al menú)while True:




while True:
    mostrarMenu()
    
 
    try:
        opcion = int (input("\tSELECCIONE ITEMS=>:→  "))
        #os.system('cls')
        match opcion:
            case 0:
                print("Saliendo")   
                exit()
            case 1:
                os.system('cls')
                print ("Agregar _ Producto")
                
                #llamon la funcion agregar producto la misma deve 
                # verificar input y si esta o no  el producto en la lista 
                    #productos = [
                    # {'codigo': '001','nombre': 'PAPA','descripcion': 'DESCRIPCION','stock': 52,'precio': 10.0},
                    # {'codigo': '002','nombre': 'TORNILLO','descripcion': 'DESCRIPCION','stock': 10, 'precio': 15.0},
                    # #]
                try:
                    opcion = input("Seleccione opción \n1) Agregar  \n2) Regresar \n0) para salir): ")
                    match opcion:
                        case '0':
                            print("Saliendo")
                        
                        case '1':
                            print("Agregar producto")
                            # Aquí debes incluir la lógica para agregar un producto
                            
                        case '2':
                            print("Regresando al menú principal")
                        case _:
                            print("Opción no válida. Ingresa 1, 2 o 0 para salir.")
                except UnicodeEncodeError:
                            print("Error: Ingresa un valor válido.")
                except ValueError:
                            print("Error: Ingresa un valor válido.")
                        
                    
                    
            case 2:
                os.system('cls')
                print ("Modificar producto")
                try:
                    opcion = input("Seleccione opción \n1) Agregar  \n2) Regresar \n0) para salir): ")
                    match opcion:
                        case '0':
                            print("Saliendo")
                        
                        case '1':
                            print("Modificar _ Producto")
                            # Aquí debes incluir la lógica para agregar un producto
                            
                        case '2':
                            print("Regresando al menú principal")
                        case _:
                            print("Opción no válida. Ingresa 1, 2 o 0 para salir.")
                except UnicodeEncodeError:
                            print("Error: Ingresa un valor válido.")
                except ValueError:
                            print("Error: Ingresa un valor válido.")
                        
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
