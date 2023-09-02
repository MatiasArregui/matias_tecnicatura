import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as MessageBox

# Permitir ingresar el punto decimal.
# Permitir ingresar números solo en las posiciones diferentes de la siete.
def validarEntrada(entrada, texto):
    print(f"Caracter de entrada: {entrada}")
    print(f"Texto en caja: {texto}")
    if len(texto) == 8:
        if entrada !=".":
            return False
    if len(texto) >10:
        return False
    
    
    return True


# Validar que el entry contenga un valor mayor a 0 y menor o igual a 999999.99.
# Validar Decimal: Desarrollar un formulario para validar un importe de 7 enteros y 2 decimales con 
# punto para separador decimal.
def validacion():
    if 999999.99 > float(entrada.get()) > 0:
        MessageBox.showerror("ERROR","Valor inadecuado")
    else:
        MessageBox.showinfo("OK", "Bien hecho")


root=tk.Tk()
root.geometry("500x600+10+10")
root.title("Ejercicio 2")
icono=tk.PhotoImage(file="logocarenacirculo.png")
root.iconphoto(True, icono)
root.config(bg="#00f0f0")
# Insertar un control entry.
# Limitar el ingreso de datos a una longitud de 10 caracteres, 7 dígitos enteros, punto decimal y dos dígitos decimales.
entrada=ttk.Entry(root, width=10,
                  validate="key",
                  validatecommand=(root.register(validarEntrada), "%S", "%P"))
# entrada["validatecommand"]=(entrada.register(funcion),"%s")
entrada.grid(column=0, row=0, padx=10,pady=10)
# Insertar un control Button.
# Asignar un texto a text.
# Asignar una función a command.
boton=ttk.Button(root, text="validar", command=validacion)
boton.grid(column=1,row=0,padx=10,pady=10)





root.mainloop()
