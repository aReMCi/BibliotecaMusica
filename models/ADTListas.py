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

    def eliminar(self, dato):
        actual = self.primero
        while actual:
            if (actual.Titulo == dato) or (actual.Artista == dato):
                if actual.anterior:
                    actual.anterior.siguiente = actual.siguiente
                else:
                    self.primero = actual.siguiente
                if actual.siguiente:
                    actual.siguiente.anterior = actual.anterior
                else:
                    self.cola = actual.anterior
                return True
            actual = actual.siguiente
        return False

    def buscar(self, dato):
        actual = self.primero
        while actual:
            if (actual.Titulo == dato) or (actual.Artista == dato):
                return {
                    'Artista': actual.Artista,
                    'Título': actual.Titulo,
                    'Duración': actual.Duracion
                }
            actual = actual.siguiente