# Escriba un programa que permita crear una lista de palabras. Para ello, el programa tiene que pedir un número y 
# luego solicitar ese número de palabras para crear la lista. Por último, el programa tiene que escribir la lista.
cont=0
lista=[]
entrada=int(input("Ingrese el numero de palabras:\n"))
if entrada == 0:
    print("Programa finalizado")
while cont<entrada:
        cont+=1
        palabra=input("Ingrese la palabra:\n")
        lista.append(palabra)
if cont>=1:
    print(lista)