from os import system
system("cls")
import random
def mayorMenorPosicion(lista):
    menor=99
    mayor=0
    for num in lista:
        
        if num > mayor:
            mayor=num
        if num < menor:
            menor=num
    return print(f"El numero mayor es: {mayor} y esta en la posicion: {lista.index(mayor)}\nEl numero menor es: {menor} y esta en la posicion: {lista.index(menor)} ")
# Generar una lista V1 de 20 elementos enteros de hasta 2 dígitos.
lista1=random.sample(range(99),20)
lista2=[]
lista3=[]
#print(lista1)
# Obtener una lista V2 a partir del lista V1 con los elementos divisibles por 2.
for num in lista1:
    if num %2 ==0:
        #print(num%2)
        lista2.append(num)
    else:
        lista3.append(num)

print(f"Lista original: {lista1}\nLista de los divisibles por 2: {lista2}\nLista de los divisibles por 3: {lista3}")
# Obtener una lista V3 a partir de la lista V1 con los elementos no divisibles por 2.
# Calcular el mayor, menor elemento y sus posiciones de la lista V2.
print("\nEl mayor, menor elemento y sus posiciones de la lista V2:")
mayorMenorPosicion(lista2)
# Calcular el mayor, menor elemento y sus posiciones de la lista V3.
print("\nEl mayor, menor elemento y sus posiciones de la lista V3:")
mayorMenorPosicion(lista3)


# Mostrar los resultados.
