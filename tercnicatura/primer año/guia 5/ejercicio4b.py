from colorama import init, Back,Fore,Style
init(True)

texto=''' La historia presenta a un narrador anónimo obsesionado con el ojo enfermo (que llama "ojo de buitre") 
de un anciano con el cual convive. Finalmente decide asesinarlo. El crimen es estudiado cuidadosamente y, 
tras ser perpetrado, el cadáver es despedazado y escondido bajo las tablas del suelo de la casa. La policía 
acude a la misma y el asesino acaba delatándose a sí mismo, imaginando alucinadamente que el corazón del viejo 
se ha puesto a latir bajo la tarima. 
'''
print(texto)
articulos={"la":0,"el":0,"los":0,"las":0,"un":0,"una":0,"unos":0,"unas":0}
for palabra in articulos:
    indice=0
    while indice<len(texto):
        buscar= texto.upper().find(" " + palabra.upper() + " ", indice)
        if buscar > -1:
            print(f"se encontro {palabra} en la posicion: {buscar}")
            indice=buscar+1
            articulos[palabra]+=1
        else:
            break
for llave, valor in articulos.items():
    print(f"cantidad de apariciones de la palabra {llave} {valor}")