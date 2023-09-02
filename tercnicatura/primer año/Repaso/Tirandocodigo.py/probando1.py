texto="matias se olviddo @como% &hacer# codigo correctamente porque viajo a neuquen a conocer a menem mientras miraba a unos seres terrorificos"
lista1=texto.split()
texto2="".join(lista1)
# print(lista1)
# print(texto2)
def buscadorPolindromos(texto):
    lista=texto.split()
    listanew=[]
    for x in lista:
        if x == x[::-1]:
            listanew.append(x)
    return listanew

# lista2=buscadorPolindromos(texto)
# print(lista2) 
# # print(lista1[1][::-1])

def limpiadorLetras(texto):
    lista=texto.split()
    for indice, palabra in enumerate(lista):
        if not palabra[0].isalnum():
            palabra=palabra[1:]
            lista[indice]=palabra
        if not palabra[-1].isalnum():
            palabra=palabra[:-1]
            lista[indice]=palabra
    return lista

listarara=limpiadorLetras(texto)
print(listarara)
        