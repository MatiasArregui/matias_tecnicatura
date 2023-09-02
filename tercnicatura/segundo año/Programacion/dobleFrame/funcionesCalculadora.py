from tkinter import messagebox as MessageBox

def validadorTeclas(entrada, cajaTexto):
    if not entrada.isdigit():
        return False
    if len(cajaTexto) >7:
        return False
    
    return True

def multiplicacion(val1, val2, resultado):
    try:
        resultado.set(str(float(val1.get())*float(val2.get())))
    except:
        resultado.set("ERROR")
        MessageBox.showerror("ERROR", "Utilize la funcion 'LIMPIAR' e ingrese valores numericos a ambos campos")

def division(val1, val2, resultado):
    try:
        valor=(f"{float(val1.get())/float(val2.get()):.2f}")
        resultado.set(valor)
    except:
        resultado.set("ERROR")
        MessageBox.showerror("ERROR", "Utilize la funcion 'LIMPIAR' e ingrese valores numericos a ambos campos")

def suma(val1, val2, resultado):
    try:
        resultado.set(str(float(val1.get())+float(val2.get())))
    except:
        resultado.set("ERROR")
        MessageBox.showerror("ERROR", "Utilize la funcion 'LIMPIAR' e ingrese valores numericos a ambos campos")

def resta(val1, val2, resultado):
    try:
        resultado.set(str(float(val1.get())-float(val2.get())))
    except:
        resultado.set("ERROR")
        MessageBox.showerror("ERROR", "Utilize la funcion 'LIMPIAR' e ingrese valores numericos a ambos campos")

def promedio(val1, val2, resultado):
    try:
        resultado.set(str((float(val1.get())*float(val2.get()))/100))
    except:
        resultado.set("ERROR")
        MessageBox.showerror("ERROR", "Utilize la funcion 'LIMPIAR' e ingrese valores numericos a ambos campos")

def limpiar(val1, val2, resultado):
    val1.set("")
    val2.set("")
    resultado.set("")