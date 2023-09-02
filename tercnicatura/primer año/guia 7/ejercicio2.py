# Crear una función para mostrar todos los elementos de una lista cualquiera y su posición, llamarla desde el main para mostrar v1 y v2.
def mostrar(lista):
    for x,y in enumerate(lista):
        print(f"Posicion: {x} Elemento: {y}")
        
# Crear una función para encontrar el mayor, menor y el promedio de un lista cualquiera, llamar desde el main para mostrar los resultados de v1 y v2.
def minMaxProm(lista):
    minimo=min(lista)
    maximo=max(lista)
    prom= sum(lista)/len(lista)
    print(f"Valor minimo: {minimo} Valor maximo: {maximo} Promedio: {prom:.2f}")

# Generar una lista de 30 elementos enteros al azar entre 50 y 250 inclusivos y guardarlos en una lista v1 (random.sample).
import random
listaRandom= random.sample(range(50,251), 30)
#print(listaRandom)
# Hacer una copia en una segunda lista v2 con los valores del primero que se encuentren entre 75 y 225 (aplicar sintaxis por comprensión).
v2=[x for x in listaRandom if x > 75 and x < 225]
# print(v2)
print("\nLISTA 1")
mostrar(listaRandom)
print("\nLISTA 2")
mostrar(v2)
print("\nLista 1")
minMaxProm(listaRandom)
print("\nLista 2")
minMaxProm(v2)
# print(sum(listaRandom))
# print(sum(v2))
