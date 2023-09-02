def ordendor(lista1,lista2):
    """ordenador: ordena dos listas ordenadas en una

    Args:
        lista1 (enteros): lista ordenada de enteros
        lista2 (enteros): lista ordenada de enteros
    """
    a=0
    b=0
    listaOrdenada=[]
    while a < len(lista1) and b<len(lista2):
        if lista1[a] < lista2[b]:
            listaOrdenada.append(lista1[a])
            a+=1
        else:
            listaOrdenada.append(lista2[b])
            b+=1
    listaOrdenada.extend(lista1[a:])
    listaOrdenada.extend(lista2[b:])
    return listaOrdenada
from random import *
david=sorted(sample(range(100),10))
abril=sorted(sample(range(100),8))
# print(david)
# print(abril)
print(ordendor(david,abril))