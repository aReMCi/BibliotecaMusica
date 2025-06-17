import tkinter as tk
from models.model import DataModel as Model
from views.view import View
from controllers.controller import Controller

ventana = tk.Tk()

#Crear el modelo, vista y controlador
model = Model()
view = View(ventana)
controller = Controller(model, view)

if __name__ == "__main__":
    ventana.mainloop()   
