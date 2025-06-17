from tkinter import Frame, Label, Button, Entry, Listbox, ttk

class View:
    def __init__(self, master):
        self.master = master
        master.title("Biblioteca de Música")
        master.geometry("600x400")
        master.config(bg="#0000FF")

        self.frame = Frame(master)
        self.frame.pack()

        self.tree = ttk.Treeview(self.frame, columns=("Artista", "Título", "Duración"), show='headings')
        self.tree.heading("Artista", text="Artista")
        self.tree.heading("Título", text="Título")
        self.tree.heading("Duración", text="Duración")
        self.tree.column("Artista", width=150)
        self.tree.column("Título", width=150)   
        self.tree.column("Duración", width=100)
        self.tree.grid(row=4, column=0, columnspan=2, padx=2, pady=2)

        #Incializacion de botones
        self.on_add_music_button = None

        #Etiquetas
        self.titulo = Label(self.frame, text="Biblioteca de Música", font=("Arial", 16))
        self.titulo.grid(row=0, column=0, columnspan=2, pady=10)

        #Entradas
        self.Artista_Entry = Entry(self.frame, width=30)
        self.Artista_Entry.grid(row=1, column=1, padx=2, pady=2)
        self.Artista_Label = Label(self.frame, text="Artista:")
        self.Artista_Label.grid(row=1, column=0, padx=2, pady=2)
        self.Titulo_Entry = Entry(self.frame, width=30)
        self.Titulo_Label = Label(self.frame, text="Título:")
        self.Titulo_Label.grid(row=2, column=0, padx=2, pady=2)
        self.Titulo_Entry.grid(row=2, column=1, padx=2, pady=2)
        self.Duracion_Entry = Entry(self.frame, width=30)
        self.Duracion_Label = Label(self.frame, text="Duración:")
        self.Duracion_Label.grid(row=3, column=0, padx=2, pady=2)
        self.Duracion_Entry.grid(row=3, column=1, padx=2, pady=2)

        #Boton para añdir musica
        self.add_music_button = Button(self.frame, text="Añadir Música", command= self._handle_add_music_button_click)
        self.add_music_button.grid(row=5, column=0, padx=2, pady=2)
        
    def _handle_add_music_button_click(self):
        if self.on_add_music_button_click:
            Titulo = self.Titulo_Entry.get()
            Artista = self.Artista_Entry.get()
            Duracion = self.Duracion_Entry.get()
            self.on_add_music_button(Titulo, Artista, Duracion)
        else:
            print("No se ha definido la acción para el botón de añadir música.")