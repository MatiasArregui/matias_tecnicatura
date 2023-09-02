# Ejercicio 2
# Escribir una función que pida un número entero entre 1 y 10, 
# lea el fichero tabla-n.txt con la tabla de multiplicar de ese número, donde n es el número introducido, 
# y la muestre por pantalla. Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello.
from pathlib import Path

def numero_entero()->int:
    while True:
        try:
            entrada=int(input("Ingrese un numero entre el 1 y el 10: "))
            if entrada<1 or entrada>10:
                print("ingreso incorrecto, ingrese un caracter entre 1 y 10")
                continue
            else:
                print("ingreso correcto")
                return entrada
                break
        except:
            print("Ingreso incorrecto")
            
numero=numero_entero()
print(f"numero: {numero}")

