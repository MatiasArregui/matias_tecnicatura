# Escriba un programa que permita crear dos listas de palabras y que, a continuación,
#  escriba las siguientes listas (en las que no debe haber repeticiones):
# Lista de palabras que aparecen en las dos listas.
# Lista de palabras que aparecen en la primera lista, pero no en la segunda.
# Lista de palabras que aparecen en la segunda lista, pero no en la primera.
# Lista de palabras que aparecen en ambas listas.
# Nota: Para evitar las repeticiones, el programa deberá empezar eliminando los elementos repetidos en cada lista.
def craedorListasPalabras():
    listaPalabras=[]
    while True:
        entrada=input("INGRESE LA PALABRA QUE FORMARA PARTE DE LA LISTA:\n")
        if entrada=="":
            print("programa finalizado")
            break
        else:
            listaPalabras.append(entrada)
    return listaPalabras

def limpiaRepetidosLista(lista):
    # Nota: Para evitar las repeticiones, el programa deberá empezar eliminando los elementos repetidos en cada lista.
    for indice,elemento in enumerate(lista):
        n=lista.index(elemento)+1
        for x in lista[indice+1:]:
            if elemento == x:
                lista.pop(lista.index(x,n))
    return lista
   
lista1=craedorListasPalabras()
lista2=craedorListasPalabras()
limpiaRepetidosLista(lista1)
limpiaRepetidosLista(lista2)

def funcionAnalizadora(lista1,lista2):
    # Lista de palabras que aparecen en las dos listas.
    listaDosListas=[]
    for x in lista1:
        if not x in listaDosListas:
            listaDosListas.append(x)
    for x in lista2:
        if not x in listaDosListas:
            listaDosListas.append(x)
    # Lista de palabras que aparecen en la primera lista, pero no en la segunda.
    listaUnoNoDos=[x for x in lista1 if not x in lista2]
    # Lista de palabras que aparecen en la segunda lista, pero no en la primera.
    listaDosNoUno=[x for x in lista2 if not x in lista1]
    # Lista de palabras que aparecen en ambas listas.
    listaAmbasListas=[x for x in lista1 if x in lista2]
    listaTotal=[]
    listaTotal.append(listaDosListas)
    listaTotal.append(listaUnoNoDos)
    listaTotal.append(listaDosNoUno)
    listaTotal.append(listaAmbasListas)
    return listaTotal

listaCompleta=funcionAnalizadora(lista1,lista2)
print(f"Valores de ambas listas: {listaCompleta[0]}\nValores de la primera lista exclucivos: {listaCompleta[1]}\nValores de la segunda lista exclusivos: {listaCompleta[2]}\nEstan en ambas listas: {listaCompleta[3]}")
listaAmbasListas=listaCompleta[0].copy()
print(listaAmbasListas)





