texto=texto2="77 01 22  neuquen De acuerdo con las estadísticas de Glassdoors, en Estados Unidos, un programador Python tiene un salario promedio anual de US$77,000, pero los experimentados puede llegar a ganar alrededor de los US$107,000. 77 22"
vector1=texto.split()
lista1=texto.split()
acentos=["á","é","í","ó","ú"]
texto3=texto[::-1]
listacompararcapicuas=texto3.split()
listaPalindromos=texto3.split()
# print(listacomparar)
for x in texto:
    if x.lower() == "á":
        texto2=texto2.replace(x, "a")
    if x.lower() == "é":
        texto2=texto2.replace(x,"e")
    if x.lower() == "í":
        texto2=texto2.replace(x,"e")
    if x.lower() == "ó":
        texto2=texto2.replace(x,"o")
    if x.lower() == "ú":
        texto2=texto2.replace(x,"u")
# print(texto)
# print(texto2)
lista2=texto.split()
lista3=[x for x in lista2 if x.isalpha()]
# print(lista3)
lista4=[x for x in lista2 if x.isnumeric()]
# print(f"lista {lista3}\nlista {lista4}")
# print()
for x in lista3:
    if x in listacompararcapicuas:
        print(f"*{x}")
    else:
        print(x)
for x in lista4:
    if x in listaPalindromos:
        print(f"*{x}")
    else:
        print(x)

# print(listacompararcapicuas)
# print(listaPalindromos)
lista123=[1,4,3,6,7]
print(lista123)
lista34453=["zarina","ariel","mateo","yan"]
print(min(lista34453,key=len))
print(min(lista123))
lista34453.sort()
lista32=[2,1,4,5,7]
lista32=sorted(lista32)
print(lista32)
listamatias=sorted([x for x in lista123])
print(listamatias)
