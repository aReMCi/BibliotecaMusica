from .ADTListas import ListaDinamicaDoble
import csv

class DataModel:
    def __init__(self):
        self.lista = ListaDinamicaDoble()

    def add_music(self, Titulo, Artista, Duracion):
        self.lista.append(Titulo, Artista, Duracion)

    def buscar_music(self, dato):
        return self.lista.buscar(dato)
    
    def eliminar_music(self, dato):
        return self.lista.eliminar(dato)

    def insertar_music(self, titulo, artista, duracion, posicion):
        self.lista.insertar(titulo, artista, duracion, posicion)

    def mostrar_lista(self):
        return self.lista.mostrar()
    
    def guardar_archivo(self, nombre_archivo):
        with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Artista', 'Título', 'Duración'])
            for item in self.lista.mostrar():
                writer.writerow([item['Artista'], item['Título'], item['Duración']])