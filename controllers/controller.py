from models.model import DataModel
from views.view import View

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        self.view.on_add_music_button_click = self.add_music
        self.view.on_search_music_button_click = self.buscar_music
        self.view.on_delete_music_button_click = self.eliminar_music

    def music_list(self):
        return self.model.mostrar_lista()
    
    def add_music(self, Titulo, Artista, Duracion):
        if Titulo and Artista and Duracion:
            self.model.add_music(Titulo, Artista, Duracion)
            self.view.update_treeview(self.music_list())
        else:
            raise ValueError("Por favor complete todos los campos.")
        
    def buscar_music(self, dato):
        if dato:
            resultado = self.model.buscar_music(dato)
            if resultado:
                return resultado
            else:
                raise ValueError("La música no se encuentra en la lista.")
        else:
            raise ValueError("Por favor ingrese un dato válido para buscar.")
        
    def eliminar_music(self, dato):
        if dato:
            if self.model.eliminar_music(dato):
                self.view.update_treeview(self.music_list())
            else:
                raise ValueError("La música no se encuentra en la lista.")
        else:
            raise ValueError("Por favor ingrese un dato válido para eliminar.")
        

        
