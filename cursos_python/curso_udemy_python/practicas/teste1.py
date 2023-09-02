import tkinter
import tkinter as tk
from tkinter import ttk

class Ventana:
    def __init__(self, ancho, alto, titulo):
        self.alto=alto
        self.ancho=ancho
        self.titulo=titulo
        self.root=tk.Tk()
        self.root.geometry(str(ancho)+ "x" +str(alto))
        self.root.title(str(titulo))
        self.root.mainloop()
        
        