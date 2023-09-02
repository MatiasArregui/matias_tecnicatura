from os import system
system("cls")
from colorama import init, Fore, Back, Style
init(True)

# A partir de un texto:
texto='''La historia presenta a un narrador anónimo obsesionado con el ojo enfermo (que llama "ojo de buitre") 
de un anciano con el cual convive. Finalmente decide asesinarlo. El crimen es estudiado cuidadosamente y, 
tras ser perpetrado, el cadáver es despedazado y escondido bajo las tablas del suelo de la casa. La policía 
acude a la misma y el asesino acaba delatándose a sí mismo, imaginando alucinadamente que el corazón del viejo 
se ha puesto a latir bajo la tarima. 
'''
cont=contla=contel=contlos=contlas=contun=contuna=contunos=contunas=0
# Mostrar en pantalla la cadena completa.
print(texto)
textoLista=texto.split()
articulos={"LA":0,"EL":0,"LOS":0,"LAS":0,"UN":0,"UNA":0,"UNOS":0,"UNAS":0}
# Encontrar cada unos de los artículos de la lista (el, la, los, las, un, una, unos, unas)
for llave, valor in articulos.items():
    
    if llave in texto.upper():
        if llave == "LA":
            articulos["LA"]=+1
            print(f"el articulo {llave} esta en la posicion: {texto.upper().find(llave, contla)}")
            contla=texto.upper().find(llave, contla) + 1
        if llave == "EL":
            articulos["EL"]=+1
            print(f"el articulo {llave} esta en la posicion: {texto.upper().find(llave, contel)}")

        if llave == "LOS":
            articulos["LOS"]=+1
            print(f"el articulo {llave} esta en la posicion: {texto.upper().find(llave, contlos)}")

        if llave == "LAS":
            articulos["LAS"]=+1
            print(f"el articulo {llave} esta en la posicion: {texto.upper().find(llave, contlas)}")

        if llave == "UN":
            articulos["UN"]=+1
            print(f"el articulo {llave} esta en la posicion: {texto.upper().find(llave, contun)}")

        if llave == "UNA":
            articulos["UNA"]=+1
            print(f"el articulo {llave} esta en la posicion: {texto.upper().find(llave, contuna)}")

        if llave == "UNOS":
            articulos["UNOS"]=+1
            print(f"el articulo {llave} esta en la posicion: {texto.upper().find(llave, contunos)}")

        if llave == "UNAS":
            articulos["UNAS"]=+1
            print(f"el articulo {llave} esta en la posicion: {texto.upper().find(llave, contunas)}")
            
        

            
        
        

print(articulos)     

# e imprimir el artículo y la posición dentro de la cadena de cada aparición.

    
# Contar y mostrar cuantos artículos de cada uno se encontraron.
