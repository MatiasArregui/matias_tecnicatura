# Escriba un programa que permita crear una lista de palabras y que, a continuación, 
# cree una segunda lista igual a la primera, pero al revés 
# (no se trata de escribir la lista al revés, sino de crear una lista distinta).
# texto="Sobre la montaña florida Sueltan los caballos En el cielo otoñal"
# lista1=texto.split()
# lista2=[x for x in reversed(lista1)]
#Lista al reves en todo sentido
#  lista2=[x[::-1] for x in reversed(lista1)]
lista1=[]
print("ingrese una o las palabras para la lista:")
while True:
    entrada=input()
    if entrada != "":
        lista1.append(entrada)
    else:
        print("Programa finalizado")
        break
if len(lista1) >0:
    lista2=[x for x in reversed(lista1)]
    #otra forma
    #lista2=lista1
    #lista2.reverse()
    print(f"lista1: {lista1}\nlista2: {lista2}\n")
else:
    print(f"No se ingresaron palabras a la lista")