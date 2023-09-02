from os import system
system("cls")
from colorama import init, Style, Cursor, Back, Fore
init(True)

texto='''La historia presenta a un narrador anónimo obsesionado con el ojo enfermo (que llama "ojo de buitre") 
de un anciano con el cual convive. Finalmente decide asesinarlo. El crimen es estudiado cuidadosamente y, 
tras ser perpetrado, el cadáver es despedazado y escondido bajo las tablas del suelo de la casa. La policía 
acude a la misma y el asesino acaba delatándose a sí mismo, imaginando alucinadamente que el corazón del viejo 
se ha puesto a latir bajo la tarima.
'''
cont=posicion=0
while True:
    print(texto)
    palabra=input("\ningrese la palabra que desea buscar: \n").upper()
    
    if palabra == "":
        print("fin del programa")
        break
    buscarPalabra=texto.upper().find(palabra.upper(), posicion)

    while buscarPalabra != -1:
        posicion=buscarPalabra+1
        print(f"se encontro la palabra {Fore.RED}{Back.GREEN}{palabra} en la ubicacion: {buscarPalabra}")
        buscarPalabra= texto.upper().find("" + palabra + "", posicion)
    else:
        print(f"Palabra no encontrada: {palabra}")