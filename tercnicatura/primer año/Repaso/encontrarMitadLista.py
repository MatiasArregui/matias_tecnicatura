from os import system
system("cls")
def intercambio(lista):
    valor=len(lista)
    listaNueva=[]
    if valor%2==0:
        valor=valor/2
        listaNueva.extend(lista[valor-1:valor+1])
    elif valor%3==0:
        valor=int(valor/2)
        listaNueva.append(lista[valor])
    else:
        valor=int(valor/2)
        listaNueva.append(lista[valor])
    return listaNueva
lista1=["matias","nicolas","mateo"]
print(intercambio(lista1))