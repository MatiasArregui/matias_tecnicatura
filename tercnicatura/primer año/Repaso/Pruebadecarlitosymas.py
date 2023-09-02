# lista=["0matias","1nicolas","2arregui","3clain","4tuki","5neuquen","622","7123"]
# for x in lista:
#     if x==x[::-1]:
#         print(f"capicua {x[::-1]}")

# print(lista[7:0:-1])
# print(lista[0:7:1])
# lista1=["matias","nicolas","arregui"]
# for indice,palabra in enumerate(lista1):
#     print(indice,palabra)
#     lista1[indice]="nicolas"
#     print(lista1)
from os import system
system("cls")

def limpiarInicioFinal(texto):
    lista1=texto.split()
    for indice,palabra in enumerate(lista1):
        if not palabra[0].isalnum():
            lista1[indice]=palabra[1:]
            palabra=palabra[1:]
        if not palabra[-1].isalnum():
            lista1[indice]=palabra[:-1]
            palabra=palabra[:-1]
    textoNuevo=" ".join(lista1)
    texto=textoNuevo
    return texto

def limpiarMedio(texto):
    lista1=texto.split()
    for indice,palabra in enumerate(lista1):
        for x in palabra[1:-1]:
            if not x.isalnum():
                palabra=palabra.replace(x,"")
        lista1[indice]=palabra
    textoNuevo=" ".join(lista1)
    texto=textoNuevo
    return texto

def encontrarCapicuas(texto):
    lista1=texto.split()
    for x in lista1:
        if x == x[::-1] and x.isalpha():
            print(f"{x} es una capicua")

def encontrarPolindromas(texto):
    lista1=texto.split()
    for x in lista1:
        if x ==x[::-1] and x.isdigit():
            print(f"{x} es un polindromo")



# lista=["abril","ariana","arregui"]

# texto="matias #se& fue/ a compra (pan ess-kere neuquen 22 123 menem"

# lista= texto.split()
# for posicion, palabra in enumerate(lista):
#     if not palabra[-1].isalnum():
#         lista[posicion]= palabra[:-1]
#         palabra = palabra[:-1]
#     if not palabra[0].isalnum():
#         lista[posicion]= palabra[1:]
#         palabra = palabra[1:]
        

# print(lista)
# texto1=limpiarInicioFinal(texto)
# print(texto1)
# print()
# texto2=limpiarMedio(texto)
# print(texto2)
# encontrarCapicuas(texto)
# encontrarPolindromas(texto)
texto = 'Una cadena de bloques, conocida en inglés como blockchain, es una '\
'etiqueta que a través de una estructura de datos cuya información se agrupa '\
'en conjuntos (bloques) a los que se les añade metainformaciones relativas a '\
'otro bloque de la cadena anterior en una línea temporal para hacer un '\
'seguimiento seguro a través de grandes cálculos criptográficos. Este/ párrafo '\
'(es) para ver el- -funcionamiento *del algo-ritmo (reconocer, arenera, salas, '\
'radar, ojo, ana, ojo ala, seres)'

# Obtener una lista de palabras a partir de texto, guardar en la lista1, a partir de lista1 
# crear lista2 sin los caracteres de inicio y fin que no sean números ni letras, mostrar lista2.
def textoALista(texto):
    lista=texto.split()
    return lista
lista1=textoALista(texto)
def limpiadorDevuelveLista(lista):
    for indice,palabra in enumerate(lista):
        if not palabra[0].isalnum():
            palabra=palabra[1:]
            lista[indice]=palabra
        if not palabra[-1].isalnum():
            palabra=palabra[:-1]
            lista[indice]=palabra
    return lista
lista2=limpiadorDevuelveLista(lista1)
print(lista2)
# Crear lista3 con los elementos de lista2 que sean palíndromos 
# (leídos a derecha y revés, se lee lo  mismo) (utilizar sintaxis por comprensión).
def creadorListaComprension(lista):
    listaNueva=[x for x in lista if x==x[::-1] and len(x) > 1]
    return listaNueva
lista3=creadorListaComprension(lista2)
print(lista3)
# Crear una función de conteo que reciba como parámetro una palabra para contar y 
# mostrar cuántas veces aparece un elemento en la lista3.
def contadorElementosLista(lista,palabra):
    contador=lista.count(palabra.lower())
    return contador
def contadorElementosLista2(lista,palabra):
    cont=0
    for x in lista:
        if x.lower() == palabra.lower():
            cont+=1
    return cont
print(contadorElementosLista(lista3,"ojo"))
print(contadorElementosLista2(lista3,"OJO"))
# Desarrollar un bloque de código para solicitar al usuario que introduzca una palabra a buscar y 
# luego llamar a la función conteo pasándole esa palabra.
def buscarPalabraFind(lista):
    textoFuncion=" ".join(lista)
    while True:
        entrada=input("Ingrese la palabra a buscar: ").lower()
        if entrada == "":
            print("programa finalizado")
            break
        indice=0
        cont=0
        while True:
            buscarPalabra=textoFuncion.find(""+entrada+"",indice)
            if buscarPalabra ==-1 and indice==0:
                print("Esa palabra no se encuentra")
                break
            if buscarPalabra==-1 and indice>0:
                break
            if buscarPalabra !=-1:
                cont+=1
                indice+=buscarPalabra+1
        print(f"La palabra {entrada} se encuentra en la lista {cont} veces")

def contadorElementosCount(lista):
    while True:
        entrada=input("Ingrese la palabra a buscar: ").lower()
        if entrada =="":
            print("Programa finalizado")
            break
        while True:
            cont=lista.count(entrada)
            break
        print(f"La palabra {entrada} aparece {cont} veces en la lista")

# Obtener una lista4 a partir de la lista3, luego aplicar a lista4 el método sort ascendente, mostrar lista4.
def creoListaSort(lista):
    listaNueva=lista.copy()
    # listaNueva.sort(reverse=True)
    listaNueva.sort()
    return listaNueva
lista4=creoListaSort(lista3)
print(lista4)
# lista5=[x[::-1] for x in reversed(lista2)]
# print(lista2)
# print(lista5)
def suma(a: int,b:int=0)->int:
    return a+b
# print(suma(1))
def creadorListasEnteros(rango1,rango2,cantidad=0):
    from random import sample, randint
    lista=sample(range(rango1,rango2),cantidad)
    return lista
# lista45=creadorListasEnteros(0,100,12)
# print(lista45)
from random import randint,sample
lista555=[randint(0,100) for x in range(12)]
print()
print(lista555)

def ordendor(lista1,lista2):
    """ordenador: ordena dos listas ordenadas en una

    Args:
        lista1 (enteros): lista ordenada de enteros
        lista2 (enteros): lista ordenada de enteros
    """
    a=0
    b=0
    listaOrdenada=[]
    while a < len(lista1) and b<len(lista2):
        if lista1[a] < lista2[b]:
            listaOrdenada.append(lista1[a])
            a+=1
        else:
            listaOrdenada.append(lista2[b])
            b+=1
    listaOrdenada.extend(lista1[a:])
    listaOrdenada.extend(lista2[b:])
    return listaOrdenada
from random import *
david=sorted(sample(range(100),10))
abril=sorted(sample(range(100),8))
# print(david)
# print(abril)
print(ordendor(david,abril))

