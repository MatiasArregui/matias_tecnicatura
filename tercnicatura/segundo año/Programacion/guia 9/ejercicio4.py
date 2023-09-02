# - Validar Nombre: Desarrollar un formulario para validar nombres, 
# quitando los blancos de los extremos, no permitir blancos consecutivos, 
# poner en mayúscula la primera letra de cada nombre y el resto en minúscula.

# - Limitar el ingreso a 50 caracteres.
# - Permitir solo el ingreso de letras, espacios en blanco o caracteres de control.
# - No permitir ingresar blancos consecutivos, es decir solo uno a la vez.
# - Insertar un botón y validar..
# - No debe terminar ni comenzar con blanco.
# - Poner con mayúscula la primera letra de cada palabra y el resto en minúsculas.
import tkinter as tk
from tkinter import ttk
from centrarVentana import centrar

root=tk.Tk()
root.geometry(centrar(ancho=700,alto=500,app=root))
root.config(bg="#00fa00")

# - Insertar un control entry.
entrada=ttk.Entry(root,
                  validate="key",
                  validatecommand=(root.register(validacionEntrada), "%S", "%P"))
entrada.grid(column=0, row=0,padx=5,pady=5)

root.mainloop()