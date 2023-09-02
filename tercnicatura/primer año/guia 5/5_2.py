from os import system
system("cls")
from colorama import init, Back, Fore, Style
init(True)
#A partir de una cadena de texto:
texto="Matias Nicolas Arregui"
#Mostrarlo en pantalla la cadena completa.
print(texto)
#Pasar el texto a una lista de palabras.
listaTexto=[]
for l in texto:
    listaTexto.append(l)
#Recorrer la lista con la instrucción for x in lista.
#print(listaTexto)
#Determinar si la palabra o elemento comienza en mayúscula.
for x in listaTexto:
    letra=(f"{x}").upper()
    #print(letra)
    if x == letra:
        #MAYUSCULA
        print(Back.RED + letra)
    else:
        #Si empieza con mayúscula imprimir en color rojo sino imprimir en blanco, deben formar un párrafo.
        print(Back.WHITE + x)
    

    



