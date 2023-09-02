# Escriba un programa que permita crear dos listas de palabras y que, a continuación, 
# elimine de la primera lista los nombres de la segunda lista.
def eliminadorIguales(lista1,lista2):
    for x in lista1:
        if x in lista2:
            lista1.remove(x)

#otra forma
def eliminadorIguales2(lista1,lista2):
    for x in lista1:
        if x in lista2:
            while x in lista1:
                lista1.pop(lista1.index(x))

lista1=[]
lista2=[]
print("A continuacion se crearan dos listas\n")
while True:

    entrada1=input("Ingrese la palabra para formar la pirmera lista\n").lower()
    if entrada1 !="":
        lista1.append(entrada1)
    else:
        print("\nPrimera lista terminada\n")
        break
while True:
    entrada2=input("Ingrese las palabras de la segunda lista\n").lower()
    if entrada2 != "":
        lista2.append(entrada2)
    else:
        print("lista dos terminada, se procedera a eliminar los nombres de la primera lista que esten en la segunda")
        break

# eliminadorIguales(lista1,lista2)
eliminadorIguales2(lista1,lista2)
print()
print(f"lista 1:\n{lista1}\nlista2:\n{lista2}")
