
# Validar Entero: Desarrollar un formulario para validar un importe entero de 7 dígitos.






import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as MessageBox

# Permitir solo el ingreso de números y teclas de control.
def validacionEntrada(entrada, texto):
    if entrada.isalpha():
        return False
    # Limitar el tamaño en caracteres a 7.
    if len(texto) > 7:
        return False
    
    return True

# Validar que el entry contenga un valor mayor a 0 y menor o igual a 9999999.
def validar():
    if int(entrada.get()) < 0:
        MessageBox.showerror("Error petero","Mejor mira porn hub")
    else:
        MessageBox.showinfo("Bien ahi", "Aguante x videos")



root=tk.Tk()
root.geometry("400x300+20+20") #("anchoxalto+x+y")
root.title("Ejercicio 1")
icono=tk.PhotoImage(file="logocarenacirculo.png")
root.iconphoto(True, icono)
root.config(bg="#00fa00")
# Utilizar un control entry.
entrada=ttk.Entry(root, width=10, 
                  validate="key",
                  validatecommand=(root.register(validacionEntrada), "%S","%P"))
entrada.grid(column=0,row=0,padx=10,pady=10)
# Insertar un control Button.
# Asignar un texto a text.
# Asignar una función a command.
boton=ttk.Button(root, text="validar", command=validar)
boton.grid(column=1, row=0, padx=5,pady=5)



root.mainloop()