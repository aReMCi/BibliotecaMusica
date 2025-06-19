from tkinter import Frame, Label, Button, Entry, Listbox, ttk, messagebox,Tk, Menu

class View:
    def __init__(self, master):
        self.master = master
        master.title("Biblioteca de Música")
        master.geometry("600x400")
        master.config(bg="#0000FF")

        self.frame = Frame(master)
        self.frame.pack()

        #Lista de música
        self.tree = ttk.Treeview(self.frame, columns=("Artista", "Título", "Duración"), show='headings')
        self.tree.heading("Artista", text="Artista")
        self.tree.heading("Título", text="Título")
        self.tree.heading("Duración", text="Duración")
        self.tree.column("Artista", width=150)
        self.tree.column("Título", width=150)   
        self.tree.column("Duración", width=100)
        self.tree.grid(row=4, column=0, columnspan=2, padx=2, pady=2)

        # Menu Principal
        self.menu_bar = Menu(master)
        master.config(menu=self.menu_bar)

        # Menu Archivo
        archivo_menu = Menu(self.menu_bar, tearoff=0)
        archivo_menu.add_command(label="Salir", command=master.quit)
        self.menu_bar.add_cascade(label="Archivo", menu=archivo_menu)

        #Incializacion de Botones
        self.on_add_music_button = None
        self.on_search_music_button = None
        self.on_delete_music_button = None

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

        # Frame para los botones
        self.botones_frame = Frame(self.frame)
        self.botones_frame.grid(row=5, column=0, columnspan=2, pady=10)
        
        #Boton para añdir musica
        self.add_music_button = Button(self.botones_frame, text="Añadir Música", command= self._handle_add_music_button_click)
        self.add_music_button.pack(side="left", padx=2)

        # Botón para buscar música
        self.search_music_button = Button(self.botones_frame, text="Buscar Música", command=self._handle_search_music_button_click)
        self.search_music_button.pack(side="left", padx=2)

        # Botón para eliminar música
        self.delete_music_button = Button(self.botones_frame, text="Eliminar Música", command=self._handle_delete_music_button_click)
        self.delete_music_button.pack(side="left", padx=2)
        
    def _handle_add_music_button_click(self):
        if self.on_add_music_button_click:
            Titulo = self.Titulo_Entry.get()
            Artista = self.Artista_Entry.get()
            Duracion = self.Duracion_Entry.get()
            self.on_add_music_button_click(Titulo, Artista, Duracion)
            self.Titulo_Entry.delete(0, 'end')
            self.Artista_Entry.delete(0, 'end')
            self.Duracion_Entry.delete(0, 'end')
            messagebox.showinfo("Éxito", "Música añadida correctamente")

    def _handle_search_music_button_click(self):
        if self.on_search_music_button_click:
            dato = self.Titulo_Entry.get()
            resultado = self.on_search_music_button_click(dato)
            if resultado:
                messagebox.showinfo("Resultado de búsqueda", f"Encontrado: {resultado['Artista']} - {resultado['Título']} - {resultado['Duración']}")
            else:
                messagebox.showwarning("No encontrado", "La música no se encuentra en la lista")
            self.Titulo_Entry.delete(0, 'end')
    
    def _handle_delete_music_button_click(self):
        if self.on_delete_music_button_click:
            dato = self.Titulo_Entry.get()
            if self.on_delete_music_button_click(dato):
                messagebox.showinfo("Éxito", "Música eliminada correctamente")
            else:
                messagebox.showwarning("No encontrado", "La música no se encuentra en la lista")
            self.Titulo_Entry.delete(0, 'end')

    def update_treeview(self, music_list):
        self.tree.delete(*self.tree.get_children())
        for music in music_list:
            self.tree.insert("", "end", values=(music['Artista'], music['Título'], music['Duración']))