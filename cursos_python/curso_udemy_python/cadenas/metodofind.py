def limpiador(texto):
    lista=texto.split()
    texto1=""
    for x in lista:
        palabra=""
        for i in x:
            if i !="@":
                palabra+=i
        texto1+=" "+palabra+" "
    return texto1

def limpiador2(texto):
    lista=texto.split()
    caracteres="@$#%+}+{[}[}$'¿?¡&$%!"
    for indice, valor in enumerate(lista):
        palabra=""
        for x in valor:
            if not x in caracteres:
                palabra+=x
        lista[indice]=palabra
    
    texto1=" ".join(lista)
    return texto1
def limpiador3(texto):
    texto1=""
    caracteres="@$#%+}+{[}[}$¿?¡&$%!"
    for x in texto:
        if not x in caracteres:
            texto1+=x
    return texto1

texto="matias fue uwu  co@mprar me#rca y no tenian, asi awa neuquen menem que fue a comprar merca a otro transa"

texto2=texto[::-1]
lista1=texto.split()
lista2=[x for x in lista1 if x == x[::-1]]
lista3=[x.capitalize() for x in lista1]
texto2=" m-atias fue a c#$omprar0 -"
# texto2=texto2.strip(" m-ra0")
texto3=limpiador2(texto)
texto4=limpiador3(texto)
print(texto4)
