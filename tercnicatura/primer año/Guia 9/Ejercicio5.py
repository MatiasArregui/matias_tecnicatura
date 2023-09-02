# Escriba un programa que permita crear una lista de palabras y que, 
# a continuación, pida dos palabras y sustituya la primera por la segunda en la lista.
lista=[]
while True:
    entrada=input("ingrese la palabra a ingresar a la lista o enter para salir:\n")
    if entrada == "":
        break
    else:
        lista.append(entrada)
print(lista)
while True:
    q=input("¿Desea sustituir la posicion de una palabra por otra?: Y/N\n")
    if q.lower() == "y":
        palabra1=input("Ingrese la palabra que desea sustiruir:\n")
        if not palabra1 in lista:
            print("no esta en lista")
            continue
        else:
            palabra2=input("Ingrese la palabra que la sustituira:\n")
            lista.insert(lista.index(palabra1),palabra2)
            lista.remove(palabra1)
    if q.lower()=="n":
        print("programa finalizado")
        break
    else:
        print("Caracter no valido")
        continue
print(lista)
