

texto = "77 01 22  neuquen De acuerdo con las estadísticas de Glassdoors, en Estados Unidos, un programador Python tiene un salario promedio anual de US$77,000, pero los experimentados puede llegar a ganar alrededor de los US$107,000. 77 22"
lista1=texto.split()
lista2=[x for x in lista1]
for x in lista1:
    palabra=""
    cont=0
    for y in x:
        if y.isalnum():
            palabra+=y
            cont+=1
    if cont>0:
        lista2.insert(lista2.index(x),palabra)
        lista2.remove(x)
print(f"Lista 1:\n{lista1}")
print(f"lista2:\n{lista2}")
listrara=["memem","mateo"]
def capicua(lista):
    for x in lista:
        if x == x[::-1]:
            print(f"* {x}")
        else:
            print(x)

while True:
    palabra=input("")
    listrara.append(palabra)
    if palabra == "0":
        break
capicua(listrara)