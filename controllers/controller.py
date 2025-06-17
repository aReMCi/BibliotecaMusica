from models.model import DataModel
from views.view import View

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        self.view.on_add_music_button_click = self.add_music

    def add_music(self, Titulo, Artista, Duracion):
        if Titulo and Artista and Duracion:
            self.model.add_music(Titulo, Artista, Duracion)
            self.view.update_treeview(self.model.mostrar_lista())
        else:
            print("Por favor, complete todos los campos.")