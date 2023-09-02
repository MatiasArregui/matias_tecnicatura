from turtle import back
from colorama import init, Fore, Back, Style
init(True)

# A partir de un texto:
texto='''La historia presenta a un narrador anónimo obsesionado con el ojo enfermo (que llama "ojo de buitre") 
de un anciano con el cual convive. Finalmente decide asesinarlo. El crimen es estudiado cuidadosamente y, 
tras ser perpetrado, el cadáver es despedazado y escondido bajo las tablas del suelo de la casa. La policía 
acude a la misma y el asesino acaba delatándose a sí mismo, imaginando alucinadamente que el corazón del viejo 
se ha puesto a latir bajo la tarima. 
'''
# Mostrar en pantalla la cadena completa..
print(texto)
# Pasar el texto a un vector.
vector1=texto.split()
listaArticulos=["el", "la", "los", "las", "un", "una", "unos", "unas"]
# Recorrer el vector.
for palabra in vector1:
    # Determinar si el elemento o palabra es uno de artículos (el, la, los, las, un, una, unos, unas).
    if palabra.lower() in listaArticulos:
        #y a los artículos en color rojo, deben formar un párrafo.
        print(f"{Back.RED} {palabra}")
    else:
        # Las palabras que no son artículos de la lista mostrarlas en color blanco 
        print(f"{Back.WHITE} {palabra}")
    
#if palabra.upper() == "LA" or palabra.upper() == "EL" or palabra.upper() == "LOS" or palabra.upper() == "LAS" or palabra.upper() == "UN" or palabra.upper() :
#    listaArticulos.append(palabra)
    



