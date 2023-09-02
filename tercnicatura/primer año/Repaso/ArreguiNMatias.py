# Crear una función de conteo que reciba como parámetro para contar y 
# mostrar cuántas veces aparece un elemento en la lista3.
def conteo(nombreDeLista,lista,elemento):
    contador=0
    for x in lista:
        if elemento.lower() == x.lower():
            contador+=1
    print(f"En {nombreDeLista} el elemento {elemento} aparece {contador} veces")

texto = 'Una cadena de bloques, conocida en inglés como blockchain, es una '\
'etiqueta que a través de una estructura de datos cuya información se agrupa '\
'en conjuntos (bloques) a los que se les añade metainformaciones relativas a '\
'otro bloque de la cadena anterior en una línea temporal para hacer un '\
'seguimiento seguro a través de grandes cálculos criptográficos. Este/ párrafo '\
'(es) para ver el- -funcionamiento *del algo-ritmo (reconocer, arenera, salas, '\
'radar, ojo, ana, ala, seres) neuquen 22'
print(f"Texto\n{texto}\n")
# Obtener una lista de palabras a partir de texto, guardar en la lista lista1, a partir de lista1 crear 
# lista2 sin los caracteres de inicio y fin que no sean números ni letras, mostrar lista2.
lista1=texto.split()
# print(lista1)
lista2=[]
# lista2=[x.strip("() - _ , . #$Q*+{ }") for x in lista1]
for x in lista1:
    palabra=""
    for y in x:
        if y.isalnum():
            palabra+=y
    lista2.append(palabra)
print(f"Lista 2:\n{lista2}")
# Crear lista3 con los elementos de lista2 que sean palíndromos (leídos a derecha y revés, se lee lo  mismo) 
# (utilizar sintaxis por comprensión).
lista3=[x for x in lista2 if x ==x[::-1]]
# print(lista3)
# Crear una función de conteo que reciba como parámetro para contar y 
# mostrar cuántas veces aparece un elemento en la lista3.
conteo("Lista3",lista3,"NEUQUEN")
# Desarrollar un bloque de código para solicitar al usuario que introduzca una palabra a buscar y 
# luego llamar a la función conteo pasándole esa palabra.
while True:
    entrada=input("Ingrese la palabra a buscar en las listas\n")
    if entrada == "":
        print("Programa finalizado\n")
        break
    else:
        conteo("Lista1",lista1,entrada)
        conteo("Lista2",lista2,entrada)
        conteo("Lista3",lista3,entrada)

# Obtener una lista4 a partir de la lista3, luego aplicar a lista4 el método sort ascendente, mostrar lista4.
lista4=lista3
lista4.sort()
print(f"Lista 4:\n{lista4}")