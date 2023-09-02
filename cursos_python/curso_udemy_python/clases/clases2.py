from tkinter import ttk
import tkinter as tk
from ttkbootstrap import Style

def centrar(ancho, alto, app):
    x = app.winfo_screenwidth() // 2 - ancho // 2
    y = app.winfo_screenheight() // 2 - alto // 2

    posi = str(ancho) + 'x' + str(alto) + '+' + str(x) + '+' + str(y)

    return posi

class Ventana:
    def __init__(self, alto, ancho):
        self.root=tk.Tk()
        # self.root.geometry(centrar(alto, ancho, self.root))
        self.root.geometry(str(alto)+"x"+str(ancho))
        self.root.title("Ventana de prueba")
        self.estilo=Style("cosmo")
        self.frame1=ttk.Frame(self.root, border=2, borderwidth=2, relief="sunken", padding="10 10 10 10")
        self.frame1.pack()
        self.botonFrame=ttk.Button(self.frame1, text="Holas FRame").grid(column=0, row=0, padx=5, pady=5)


        self.root.mainloop()
        
if __name__ == "__main__":   
    ventanaa1=Ventana(alto=300, ancho=320)     
    print(__name__)