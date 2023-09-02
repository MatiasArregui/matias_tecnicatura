import tkinter as tk
from tkinter import ttk
from tkinter import StringVar
from centrarVentana import centrar


# METODO CONTROL A LOS DOS ENTRY

def metodoControl(entrada, texto):
    print(texto)
    print(entrada)
    if not entrada.isdigit():
        return False
    if len(texto) > 7:
        return False
    
    return True

# FUNCION LIMPIAR
def limpiar():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    resultado.set("")

# FUNCION MATEMATICA
# MULTIPLICACION
def operacionM():
    multiplicacion=float(entry1.get()) * float(entry2.get()) 
    resultado.set(multiplicacion)
    
# DIVISION
def operacionD():
    division= float(entry1.get()) / float(entry2.get())
    resultado.set(division)    

#SUMA
def operacionS():
    suma=float(entry1.get()) + float(entry2.get())
    resultado.set(suma)
    
#RESTA
def operacionR():
    resta=float(entry1.get()) - float(entry2.get())
    resultado.set(resta)
    
#PROMEDIO
def operacionProm():
    promedio=(float(entry1.get()) * float(entry2.get()))/100
    resultado.set(promedio)



root=tk.Tk()
root.geometry(centrar(ancho=300, alto=300, app=root))
root.title("Calculadora")
root.config(bg="Black")
root.resizable(0,0)

# FRAME
# frame1=ttk.Frame(root, border="")
# CREACION DEL STRINGVAR PARA EL RESULTADO
resultado=StringVar()
# frame=ttk.Frame(style=)
# ENTRADA DE DATOS UNO
entry1=ttk.Entry(root,
                 width=7,
                 validate="key",
                 validatecommand=(root.register(metodoControl), "%S","%P"))
entry1.grid(row=0,column=1,padx=5,pady=5)
label1=ttk.Label(root,text="Ingrese un valor: ")
label1.grid(row=0,column=0,padx=5,pady=5)
# ENTRADA DE DATOS DOS
entry2=ttk.Entry(root, 
                 width=7,
                 validate="key")
entry2['validatecommand']=(entry2.register(metodoControl), "$S", "$P")
entry2.grid(row=1,column=1,padx=5,pady=5)
label2=ttk.Label(root,text="Ingrese un valor: ")
label2.grid(row=1,column=0,padx=5,pady=5)
# MUESTRA DE RESULTADO
entry3=ttk.Entry(root, state="disabled",textvariable=resultado)
entry3.grid(column=1,row=2,padx=5,pady=5)
label3=ttk.Label(root, text="Resultado: ")
label3.grid(row=2,column=0,padx=5,pady=5)

# BOTON MULTIPLICAR

botonMultiplicar=ttk.Button(root,text="X",
                            command=operacionM)
botonMultiplicar.grid(row=3,column=0,padx=5,pady=5)

# BOTON DIVIDIR

botonDividir=ttk.Button(root, text="/",
                        command=operacionD)
botonDividir.grid(row=4, column=0, padx=5, pady=5)

#BOTON SUMAR

botonSuma=ttk.Button(root, text="+",
                     command=operacionS)
botonSuma.grid(row=4, column=1, padx=5, pady=5)

#BOTON RESTAR

botonRestar=ttk.Button(root, text="-",
                       command=operacionR)
botonRestar.grid(row=3, column=1,padx=5,pady=5)

#BOTON PORCENTAJE

botonPorcentaje=ttk.Button(root, text="%",
                           command=operacionProm)
botonPorcentaje.grid(row=5,column=1,padx=5,pady=5)

#BOTON LIMPIAR
botonLimpiar=ttk.Button(root,
                        text="Limpiar",
                        command=limpiar)
botonLimpiar.grid(row=5,column=0,padx=5, pady=5)

root.mainloop()