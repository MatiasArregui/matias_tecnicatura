from os import system
system("cls")
from colorama import init, Style, Cursor, Back, Fore
init(True)

#A partir de una cadena de texto:
texto='''La historia presenta a un narrador anónimo obsesionado con el ojo enfermo (que llama "ojo de buitre") 
de un anciano con el cual convive. Finalmente decide asesinarlo. El crimen es estudiado cuidadosamente y, 
tras ser perpetrado, el cadáver es despedazado y escondido bajo las tablas del suelo de la casa. La policía 
acude a la misma y el asesino acaba delatándose a sí mismo, imaginando alucinadamente que el corazón del viejo 
se ha puesto a latir bajo la tarima. 
'''
#Mostrar en pantalla la cadena completa.
print(texto)
#Añadir una estructura de control while
while True:
    #Solicitar al usuario ingrese una palabra a buscar en el texto.
    palabra=input("Ingrese la palabra o letra a buscar: \n").upper()
    #Salir con enter o sea cuando palabra es igual ‘’
    if palabra == "":
        print("PROGRAMA FINALIZADO")
        break
    else:
        #Para buscar utilizar texto.find
        busqueda=texto.upper().find(palabra)
        #Si la búsqueda devuelve -1, mostrar el cartel “La palabra no se encuentra”
        if busqueda == -1:
            print("PALABRA NO ENCONTRADA")
        else:
            #Si la palabra se encuentra mostrar el texto con la palabra coloreada en rojo.
            print(Back.RED + palabra.lower(), "estaba en la posicion:",busqueda)
    
        








