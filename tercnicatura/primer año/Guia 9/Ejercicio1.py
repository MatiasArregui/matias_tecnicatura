# Escriba una función que reciba dos listas de enteros ordenados y devuelva una sola lista ordenada; 
# no se pueden utilizar funciones de ordenamiento ni implementar ningún algoritmo de ordenamiento.
def ordenador(lista1,lista2):
    lista=lista1+lista2
    n=len(lista)
    for x in range(n-1):
        for y in range(n-1):
            if lista[y] > lista[y+1]:
                lista[y],lista[y+1]=lista[y+1],lista[y]
    return lista

from random import sample
lista1=sorted(sample(range(100),5))
lista2=sorted(sample(range(100),5))
print(ordenador(lista1,lista2))
# lista1.sort()
# lista2=sorted(lista2)
# lista3=lista1+lista2
# print(lista3)
# # lista2=lista2.sort()
# print(lista1)
# print()
# print(lista2)
# print(lista3)
