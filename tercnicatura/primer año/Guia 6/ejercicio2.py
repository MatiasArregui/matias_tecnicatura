from os import system
system("cls")
import random
def minmax(lista):
    minimo=min(lista)
    maximo=max(lista)
    posicionMin=lista.index(minimo)
    posicionMax=lista.index(maximo)
    print(f"El menor {minimo}, mayor elemento {maximo} y sus posiciones: Mayor elemento: {posicionMax} Menor elemento: {posicionMin}.")


# Generar una lista de 20 elementos enteros al azar de hasta dos dígitos.
lista1=random.sample(range(99), 20)
print(f"Lista original: {lista1}\n")
lista2=lista1[0:10]
lista3=lista1[10:20]
#print(lista2,lista3)
# Calcular el menor, mayor elemento y sus posiciones de los primeros 10.
print(f"Lista de los primeros 10 elementos: {lista2}")
minmax(lista2)
print()
print(f"Lista de los segundos 10 elementos: {lista3}")
minmax(lista3)
print()
# Calcular el mayor, menor elemento y sus posiciones de los segundos 10.
# Mostrar resultados.
