# Escriba un programa que permita crear dos listas de palabras y que, a continuación, escriba las siguientes listas 
# (en las que no debe haber repeticiones):
# Nota: Para evitar las repeticiones, el programa deberá empezar eliminando los elementos repetidos en cada lista.
def eliminaRep(lista):
    for x in lista:
        n=lista.index(x)+1
        for y in lista[n:]:
            if x == y:
                lista.pop(lista.index(y))

lista1=[]
lista2=[]
print("ingrese las palabras de la primera lista")
while True:
    entrada=input("Ingrese la palabra:\n").lower()
    if entrada !="":
        lista1.append(entrada)
    else:
        print("carga de palabras finalizado")
        break
print("ingrese las palbras de la segunda lista")
while True:
    entrada=input("Ingrese la palabra:\n").lower()
    if entrada !="":
        lista2.append(entrada)
    else:
        print("carga de palabras finalizado")
        break
# Nota: Para evitar las repeticiones, el programa deberá empezar eliminando los elementos repetidos en cada lista.
eliminaRep(lista1)
eliminaRep(lista2)
print(f"Lista 1: {lista1}\nLista 2: {lista2}")
# Lista de palabras que aparecen en las dos listas.
lista3=[x for x in lista1 if x in lista2]
print(f"\nLista de palabras que aparecen en las dos listas\n{lista3}")
# Lista de palabras que aparecen en la primera lista, pero no en la segunda.
lista4=[x for x in lista1 if not x in lista2]
print(f"\nLista de palabras que aparecen en la primera lista, pero no en la segunda\n{lista4}")
# Lista de palabras que aparecen en la segunda lista, pero no en la primera.
lista5=[x for x in lista2 if not x in lista1]
print(f"\nLista de palabras que aparecen en la segunda lista, pero no en la primera\n{lista5}")
# Lista de palabras que aparecen en ambas listas.
lista6=[x for x in lista2 if x in lista1]
print(f"\nLista de palabras que aparecen en ambas listas\n{lista6}")

