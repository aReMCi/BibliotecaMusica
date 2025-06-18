#Lista dinamica doblemente enlazada dinamica (Nodo)
class Nodo:
    def __init__(self, Titulo, Artista, Duracion):
        self.Artista = Artista
        self.Titulo = Titulo
        self.Duracion = Duracion
        self.siguiente = None
        self.anterior = None

#Lista dinamica simple dinamica (Lista)

class ListaDinamicaDoble:
    def __init__(self):
        self.primero = None
        self.cola = None

    def append(self, Titulo, Artista, Duracion):
        nuevo_nodo = Nodo(Titulo, Artista, Duracion)
        if not self.primero:
            self.primero = self.cola = nuevo_nodo
        else:
            self.cola.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.cola
            self.cola = nuevo_nodo
    
    def mostrar(self):
        actual = self.primero
        resultado = []
        while actual:
            resultado.append({
                'Artista': actual.Artista,
                'Título': actual.Titulo,
                'Duración': actual.Duracion
            })
            actual = actual.siguiente
        return resultado


    def _eliminar(self, dato):
        actual = self.primero
        while actual:
            if actual.dato == dato:
                if actual.anterior:
                    actual.anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                if actual.siguiente:
                    actual.siguiente.anterior = actual.anterior
                else:
                    self.cola = actual.anterior
                return
            actual = actual.siguiente

    def eliminar(self, dato):
        nodo = self._buscar(dato)
        if nodo:
            self._eliminar(nodo)
        else:
            raise ValueError("El dato no se encuentra en la lista")

    def buscar(self, dato):
        actual = self.primero
        while actual:
            if actual.Titulo == dato or actual.Artista == dato:
                return {
                    'Artista': actual.Artista,
                    'Título': actual.Titulo,
                    'Duración': actual.Duracion
                }
            actual = actual.siguiente

    def insertar(self, Titulo, Artista, Duracion, posicion):
        nuevo_nodo = Nodo(Titulo, Artista, Duracion)
        if posicion == 0:
            nuevo_nodo.siguiente = self.primero
            if self.primero:
                self.primero.anterior = nuevo_nodo
            self.primero = nuevo_nodo
            if not self.cola:
                self.cola = nuevo_nodo
        else:
            actual = self.primero
            for _ in range(posicion - 1):
                if actual is None:
                    raise IndexError("Posición fuera de rango")
                actual = actual.siguiente
            nuevo_nodo.siguiente = actual.siguiente
            nuevo_nodo.anterior = actual
            if actual.siguiente:
                actual.siguiente.anterior = nuevo_nodo
            else:
                self.cola = nuevo_nodo
            actual.siguiente = nuevo_nodo