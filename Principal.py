from OperBasicListasE import ListaEnlazada

# Inicializamos la lsita
lista = ListaEnlazada()

while True: 
# Menú de opciones
    print('=' * 40)
    print("Menú de opciones")
    print('=' * 40)
    print("1) Insertar un valor al incio de la lista")
    print("2) Insertar un valor al final de la lista")
    print("3) Eliminar el primer valor")
    print("4) Buscar un valor de la lista")
    print("5) Imprimir los valores de la lista")
    print("6) Salir")
    print('=' * 40)
    opc = int(input("Seleeciona una opción: "))

    match opc:
        case 1:
            valor = int(input("Ingrese un valor: "))
            lista.insertar_al_principio(valor)
            print("Valor agregado al incio de la lista correctamente")
            
        case 2:
            valor = int(input("Ingrese un valor: "))
            lista.insertar(valor)
            print("Valor agregado al incio de la lista correctamente")
            
        case 3: 
            valor = int(input("Ingrese el valor a eliminar: "))
            if lista.eliminar(valor):
                print("Valor eliminado correctamente.")
            else:
                print("El valor no se encontró en la lista.")
                
        case 4:
            valor = int(input("Ingrese el valor a buscar: "))
            if lista.buscar(valor):
                print("El valor se encuentra en la lista.")
            else:
                print("El valor NO se encuentra en la lista.")
                
        case 5:
            lista.imprimir()
        case 6:
            print("Saliendo del programa...")
            break
        
        case _:
            print("Opción no válida.")