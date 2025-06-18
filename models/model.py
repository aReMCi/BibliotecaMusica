from .ADTListas import ListaDinamicaDoble

class DataModel:
    def __init__(self):
        self.lista = ListaDinamicaDoble()

    def add_music(self, Titulo, Artista, Duracion):
        self.lista.append(Titulo, Artista, Duracion)

    def buscar_music(self, dato):
        return self.lista.buscar(dato)
    
    def eliminar_music(self, dato):
        self.lista.eliminar(dato)

    def insertar_music(self, titulo, artista, duracion, posicion):
        self.lista.insertar(titulo, artista, duracion, posicion)

    def mostrar_lista(self):
        return self.lista.mostrar()