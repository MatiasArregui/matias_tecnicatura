# Escriba un programa que permita crear una lista de palabras y que, a continuación, 
# elimine los elementos repetidos (dejando únicamente el primero de los elementos repetidos).
def elElementosRpetedidos(lista):
    for x in lista:
        if lista1.count(x) >1:
            while lista1.count(x)>1:
                lista1.pop(lista.index(x))
    return lista

print("El siguiente programa creara una lista de palabra y eliminara los elementos repetidos")
lista1=[]
while True:
    entrada=input("ingrese la palabra a agregar a la lista:\n")
    if entrada !="":
        lista1.append(entrada)
    else:
        print("Se termino de cargar las palabras a la lista\n")
        break
# print(elElementosRpetedidos(lista1))
print(f"Lista creada luego de eliminar posibles repetidos:\n{elElementosRpetedidos(lista1)}")
#otra froma
# lista2=lista1
# for x in lista2:
#     n=lista1.index(x)+1
#     for y in lista2[n:]:
#         if x == y:
#             lista2.pop(lista2.index(y))
# print(lista2)