from os import system
system("cls")
import tkinter as tk
from tkinter import StringVar, ttk
from tkinter import messagebox as MessageBox
from ttkbootstrap import Style                                                                                                                                                                                                                                                                 
from centrar_ventana import centrar



# METODO CONTROL A LOS DOS ENTRY
def controlEntrada(entrada, texto):
    print(f"Ingreso de teclado: {entrada}")
    print(f"Caja de texto: {texto}")
    if len(texto) == 8:
        return False 
    if not entrada.isdigit():
        return False
    
    return True

# FUNCION LIMPIAR
def limpiar():
    entry1Str.set("")
    entry2Str.set("")
    resultado.set("")

# FUNCIONES MATEMATICAS
# MULTIPLICACION 
def operacionM():
    try:
        resultado.set(str(float(entry1Str.get())*float(entry2Str.get())))
    except ValueError:
        MessageBox.showerror("ERROR", "Por favor, ingrese un numero")
        resultado.set("ERROR")
        
# DIVISION
def operacionD():
    try:
        resultado.set(str(float(entry1Str.get())/float(entry2Str.get())))
    except ValueError:
        MessageBox.showerror("ERROR", "Por favor, ingrese un numero")
        resultado.set("ERROR")
        

#SUMA
def operacionS():
    try:
        resultado.set(str(float(entry1Str.get())+float(entry2Str.get())))
    except ValueError:
        MessageBox.showerror("ERROR", "Por favor, ingrese un numero")
        resultado.set("ERROR")
    
#RESTA
def operacionR():
    try:
        resultado.set(str(float(entry1Str.get())-float(entry2Str.get())))
    except ValueError:
        MessageBox.showerror("ERROR", "Por favor, ingrese un numero")
        resultado.set("ERROR")
    
#PROMEDIO
def operacionProm():
    try:
        resultado.set(str((float(entry1Str.get()) * float(entry2Str.get()))/100))
    except ValueError:
        MessageBox.showerror("ERROR", "Por favor, ingrese un numero")
        resultado.set("ERROR")

# CREACION DE VENTANA
root=tk.Tk()
root.geometry(centrar(ancho=360, alto=249, app=root))
root.title("Práctico 2 - Programación II")
icono=tk.PhotoImage(file="practico2_matias_arregui\\logo.png")
root.iconphoto(True, icono)
root.resizable(False, False)

# APLICACION DE STYLE
style=Style("darkly")

#CREACION DEL FRAME
frame = ttk.Frame(root, padding='10 10 10 10', height=70, width=30, borderwidth=2, relief='sunken')
frame.pack()

# CREACION DEL STRINGVAR PARA EL RESULTADO
resultado=StringVar()
# CREACION DEL STRINGVAR PARA EL ENTRY1
entry1Str=StringVar()
# CREACION DEL STRINGVAR PARA EL ENTRY2
entry2Str=StringVar() 
# TODOS LOS "ENTRY"
# ENTRADA DE DATOS UNO
entry1=ttk.Entry(frame,
                 width=15,
                 textvariable=entry1Str,
                 validate="key",
                 validatecommand=(frame.register(controlEntrada), "%S", "%P"))
entry1.grid(row=0,column=1,padx=5,pady=5)
entry1.config(width=15)
entry1.focus()
#ASIGNACIÓN DE VALOR AL STRINGVAR DEL ENTRY1
entry1Str.set(entry1.get())

# ENTRADA DE DATOS DOS
entry2=ttk.Entry(frame, 
                 width=15,
                 textvariable=entry2Str,
                 validate="key",
                 validatecommand=(frame.register(controlEntrada), "%S", "%P"))
entry2.grid(row=1,column=1,padx=5,pady=5)
entry2.config(width=15)
#ASIGNACIÓN DE VALOR AL STRINGVAR DEL ENTRY2
entry2Str.set(entry2.get())

# ENTRADA DE DATOS TRES
entry3=ttk.Entry(frame, width=15,
                 state="disabled",
                 textvariable=resultado)
entry3.grid(column=1,row=2,padx=5,pady=5)


# TODOS LOS LABEL
# LABEL 1
label1=ttk.Label(frame,text="Valor 1: ", width=15)
label1.grid(row=0,column=0,padx=5,pady=5)

# LABEL 2
label2=ttk.Label(frame,text="Valor 2: ", width=15)
label2.grid(row=1,column=0,padx=5,pady=5)

# LABEL 3
label3=ttk.Label(frame, text="Resultado: ", width=15)
label3.grid(row=2,column=0,padx=5,pady=5)

# BOTON MULTIPLICAR

botonMultiplicar=ttk.Button(frame,text="*",
                            command=operacionM, width=15)
botonMultiplicar.grid(row=4,column=0,padx=5,pady=5)
# BOTON DIVIDIR

botonDividir=ttk.Button(frame, text="/",
                        command=operacionD, width=15)
botonDividir.grid(row=4, column=1, padx=5, pady=5)

#BOTON SUMAR

botonSuma=ttk.Button(frame, text="+",
                     command=operacionS, width=15)
botonSuma.grid(row=3, column=0, padx=5, pady=5)

#BOTON RESTAR

botonRestar=ttk.Button(frame, text="-",
                       command=operacionR, width=15)
botonRestar.grid(row=3, column=1,padx=5,pady=5)

#BOTON PORCENTAJE

botonPorcentaje=ttk.Button(frame, text="%",
                           command=operacionProm, width=15)
botonPorcentaje.grid(row=5,column=0,padx=5,pady=5)

#CAMBIO ESTILO BOTON LIMPIAR
botonEstilo=ttk.Style(frame)
botonEstilo.configure("BotonFondo.TButton", foreground="#ff0000")
#BOTON LIMPIAR
botonLimpiar=ttk.Button(frame,
                        text="Limpiar",
                        command=limpiar, width=15, style="BotonFondo.TButton")
botonLimpiar.grid(row=5,column=1,padx=5, pady=5)


# VERIFICACIONES DE OTRA MANERA
# entry1['validatecommand']=(entry1.register(controlEntrada), "%S", "%P")
# entry2['validatecommand']=(entry2.register(controlEntrada), "%S", "%P")

root.mainloop()