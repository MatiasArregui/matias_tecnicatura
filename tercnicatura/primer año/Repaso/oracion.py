def buscaRepe(juan):
    for x in juan:
        elem=juan.count(x)
        if elem > 1:
            while elem>1:
                juan.remove(x)
                elem-=1
                


lista1 = []
lista2 = []
while True:
    entrada1 = input("ingrese un valor para lista1: ")
    if entrada1=="":
        print("Lista 1 creada")
        break
    lista1.append(entrada1)

while True:
    entrada2 = input("ingrese un valor para lista2: ")
    if entrada2=="":
        print("lista 2 creada")
        break
    lista2.append(entrada2)
print(lista1)
buscaRepe(lista1)
print(lista1)
print(lista2)
buscaRepe(lista2)
print(lista2)
