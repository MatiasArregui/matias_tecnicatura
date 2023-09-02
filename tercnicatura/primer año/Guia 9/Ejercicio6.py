# Escriba un programa que permita crear una lista de palabras y que, 
# a continuación, pida una palabra y elimine esa palabra de la lista.

lista=[]
while True:
    palabra=input("Ingrese la palabra a agregar a la lista:\n")
    if palabra =="":
        print("PROGRAMA FINALIZADO")
        break
    else:
        lista.append(palabra.lower())
while True:
    removedor=input("Desea eliminar alguna palabra:Y/N\n").lower()
    if removedor == "y":
        palabraDelete=input("Ingrese la palabra a remover:\n").lower()
        if palabraDelete in lista:
            while palabraDelete in lista:
                lista.remove(palabraDelete)
        else:
            print("Esa palabra no esta en lista")
    if removedor=="n":
        break
    if "y" != removedor !="n":
        print("caracter no valido")

print(lista)