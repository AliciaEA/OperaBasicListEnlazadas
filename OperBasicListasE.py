# Programa de "Ejemplificando la creación de una lista enlazada simple"
# Desarrollado por: Sara Zambrana y Alicia Estrada :)
# Versión 1.0
# 23.abril.2025



# Clase Nodo - representa un nodo de la lista
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

# Clase ListaEnlazada - gestiona la lista y sus operaciones
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
        
    #Insertar un nuevo valor al principio de la lista
    def insertar_al_principio(self, valor):
        nuevo = Nodo(valor)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo
    
    # Método que cuenta el número de nodos en la lista
    def longitudLista(self):
        contador = 0  # Inicializa el contador en 0
        actual = self.cabeza  # Empieza desde la cabeza de la lista
        while actual:  # Recorre la lista mientras haya nodos
            contador += 1  # Incrementa el contador por cada nodo
            actual = actual.siguiente  # Avanza al siguiente nodo
        return contador  # Retorna el número total de nodos
        
    # Método para determinar si la lista está vacía
    def esta_vacia(self):
        return self.cabeza is None  # Retorna True si la cabeza es None, False en caso contrario
    
    # Insertar un nuevo valor al final de la lista
    def insertar(self, valor):
        nuevo = Nodo(valor)
        if not self.cabeza:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo

    # Eliminar el primer nodo que contenga el valor
    def eliminar(self, valor):
        actual = self.cabeza
        anterior = None

        while actual:
            if actual.valor == valor:
                if anterior:
                    anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                return True  # Valor eliminado
            anterior = actual
            actual = actual.siguiente

        return False  # Valor no encontrado

    # Método para buscar un valor en la lista
    def buscar(self, valor):
        actual = self.cabeza
        while actual:
            if actual.valor == valor:
                return True
            actual = actual.siguiente
        return False

    # Método que imprime los valores de la lista
    def imprimir(self):
        actual = self.cabeza
        if not actual:
            print("La lista está vacía")
            return
        print("Lista enlazada:", end=" ")
        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.siguiente
        print("None")
"""Esta línea asegura que el siguiente bloque solo se ejecuta si el archivo se corre directamente, y no cuando es importado como módulo en otro archivo"""
if __name__ == "__main__":
    lista = ListaEnlazada()  #Creando el objeto lista
    lista.insertar(10)
    lista.insertar(20)
    lista.insertar(30)
    lista.insertar(40)
    lista.imprimir()  # Lista: 10 -> 20 -> 30 -> 40 -> None
    print("Buscando el valor 20", lista.buscar(20))  # True
    print("Buscar el número 50?", lista.buscar(50))  # False
    lista.eliminar(30)
    lista.imprimir()  # Lista: 10 -> 20 -> 40 -> None
    lista.eliminar(10)
    lista.imprimir()  # Lista: 20 -> 40 -> None
    lista.imprimir()  # Lista: 20 -> 40 -> None
