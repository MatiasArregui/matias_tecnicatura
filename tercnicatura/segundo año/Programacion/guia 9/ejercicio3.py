import tkinter as tk
from tkinter import ttk
from centrarVentana import centrar
from tkinter import messagebox as MessageBox
# Validar Período: Desarrollar un formulario para validar un período con un formato de 
# dos lugares para el mes, guión separador y 4 lugares para el año.
def validacionEntrada(entrada, texto):
    print(f"Entrada teclado: {entrada}")
    print(f"Texto en caja: {texto}")
    # Permitir solo el ingreso de números, guión y/o teclas de control.
    if entrada.isalpha() :
        return False
    if len(texto)==3:
        if entrada !="/" and entrada.isalnum():
            return False
    if len(texto) == 8:
        return False
    
    return True


# Verificar que el año mayor o igual a 1990 y menor o igual a 2023, si no cumple mostrar la leyenda “El año no es válido”.
# Si la validación resulta exitosa, entonces mostrar la leyenda “El período es válido”.
def validacionMes():
    # Verificar que el mes esté entre 01 y 12, si no cumple mostrar la leyenda “El mes no es válido”.
    n=entrada.get()
    if (12>= int(n[0:2]) >=1):
        MessageBox.showinfo("OK", "El mes es valido")
    else:
        MessageBox.showerror("ERROR", "El mes no es valido")
    if (1990<=int(n[3:])<=2023):
        MessageBox.showinfo("OK", "El periodo es valido")
    else:
        MessageBox.showerror("ERROR","El año no es valido")




root=tk.Tk()
# Centrar el formulario.
root.geometry(centrar(ancho=300,alto=300,app=root))
root.config(bg="#0aa000")
# Insertar un control entry.
# Limitar el entry a 7 caracteres máximo.
entrada=ttk.Entry(root, width=7,
                  validate="key",
                  validatecommand=(root.register(validacionEntrada), "%S", "%P"),
                  font="Times")
entrada.grid(column=0,row=0,padx=10,pady=10)
boton=ttk.Button(root,text="Validar mes", command=validacionMes)
boton.grid(column=2,row=0,padx=10,pady=10)
# boton2=ttk.Button(root, text="Validar año", command=validacionAño)
# boton2.grid(column=3,row=0,padx=10,pady=10)


root.mainloop()