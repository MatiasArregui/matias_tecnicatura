#LIMPIAR CONSOLA
from os import system
system("cls")
#IMPORTACION BIBLIOTECAS GUI
import tkinter as tk
from tkinter import StringVar, ttk, Frame
from ttkbootstrap import Style
#IMPORTACION FUNCIONES
from centrarVentana import centrar
from funcionesCalculadora import *

#CREACION DE LA VENTANA MAIN
root=tk.Tk()
root.title("Calculadora")
root.geometry(centrar(ancho=600,alto=200, app=root))
#AGREGADO DE ICONO
icono=tk.PhotoImage(file="dobleFrame//calculadora.png")
root.iconphoto(True, icono)
#VENTANA ESTATICA
root.resizable(False, False)
#APLICACION DE ESTILO
estilo=Style("cyborg")
#FRAME 1
frame1 = ttk.Frame(root, padding='10 10 10 10', height=370, width=340, borderwidth=2, relief='solid')
frame1.pack(side='left', padx=10, pady=10)
#FRAME 2
frame2 = ttk.Frame(root, padding='10 10 10 10', height=370, width=340, borderwidth=2, relief='solid')
frame2.pack(side='right', padx=10, pady=10)
#CREACION STRINGVAR
resultado=tk.StringVar(frame1, "RESULTADO")
val1=tk.StringVar()
val2=tk.StringVar()
#CREACION DE COMPONENTES DEL FRAME 1

#ENTRY 1 Y SU STRINGVAR
entry1=ttk.Entry(frame1, textvariable=val1, width=15,
                 validate="key",
                 validatecommand=(frame1.register(validadorTeclas), "%S", "%P"))
entry1.grid(column=1, row=0, padx=5, pady=5)
val1.set(entry1.get())

#LABEL ENTRY 1
label1=ttk.Label(frame1, text="Valor 1", width=15)
label1.grid(column=0, row=0, padx=10, pady=10)

#ENTRY 2 Y SU STRINGVAR
entry2=ttk.Entry(frame1, textvariable=val2, width=15,
                 validate="key",
                 validatecommand=(frame1.register(validadorTeclas), "%S", "%P"))
entry2.grid(column=1, row=1, padx=5, pady=5)
val2.set(entry2.get())

#LABEL ENTRY 2
label2=ttk.Label(frame1, text="Valor 2", width=15)
label2.grid(column=0, row=1, padx=10, pady=10)

#ENTRY 3 Y SU STRINGVAR
entry3=ttk.Entry(frame1, textvariable=resultado, justify="center",state="disabled", width=15)
entry3.grid(column=1, row=2, padx=10, pady=10)

#LABEL ENTRY 3
label3=ttk.Label(frame1, text="Resultado", width=15)
label3.grid(column=0, row=2, padx=10, pady=10)

#CREACION DE COMPONENTES DEL FRAME 2

#BOTONES
#Boton 1
boton1=ttk.Button(frame2, text="*", command=lambda: multiplicacion(val1, val2, resultado), width=15)
boton1.grid(column=0, row=0, padx=10, pady=10)
#Boton 2
boton2=ttk.Button(frame2, text="/", command=lambda: division(val1, val2, resultado), width=15)
boton2.grid(column=0, row=1, padx=10, pady=10)
#Boton 3
boton3=ttk.Button(frame2, text="+", command=lambda: suma(val1, val2, resultado), width=15)
boton3.grid(column=0, row=2, padx=10, pady=10)
#Boton 4
boton4=ttk.Button(frame2, text="-", command=lambda: resta(val1, val2, resultado), width=15)
boton4.grid(column=1, row=0, padx=10, pady=10)
#Boton 5
boton5=ttk.Button(frame2, text="%", command=lambda: promedio(val1, val2,resultado), width=15)
boton5.grid(column=1, row=1, padx=10, pady=10)
#Boton 6
boton6=ttk.Button(frame2, text="Limpiar", command=lambda: limpiar(val1, val2, resultado), width=15)
boton6.grid(column=1, row=2, padx=10, pady=10)


root.mainloop()