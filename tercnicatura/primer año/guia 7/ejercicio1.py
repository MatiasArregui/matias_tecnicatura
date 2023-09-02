from os import system
system("cls")
from colorama import init, Back, Fore
init(True)
# A partir de una cadena de texto iniciada en el código, mostrar la cadena en color azul.
texto="Need for speed es un juego de carreras que se basa en autos modificados y carreras clandestinas en un mundo abierto de 400 jugadores"
# Crear un nuevo_texto con los caracteres que sean solo letras y espacios, mostrar nuevo_texto en color blanco 
# (aplicar join combinado con sintaxis por comprensión para filtrar o filter).
nuevo_texto="".join([x for x in texto.lower() if (x <= "z" and x >= "a") or x == " " ])
print("Texto Original\n",texto)
# Convertir el texto en una lista de palabras y mostrar todos los elementos y su posición en color blanco (enumerate).
print("Convertir el texto en una lista de palabras y mostrar todos los elementos y su posición en color blanco\n")
newTexto=texto.split()
for pos, val in enumerate(newTexto):
    print(f"Posicion: {pos} Palabra: {val}")
# Encontrar y mostrar el elemento menor, mayor y su posición en la lista de palabras 
# (min, max e index, min y max deben proporcionar el argumento key = len para comparar cadenas).
minimo=min(newTexto,key=len)
maximo=max(newTexto,key=len)
print("\nEncontrar y mostrar el elemento menor, mayor y su posición en la lista de palabras ")
print(f"Elemento mayor: '{maximo}' y su posicion: {newTexto.index(maximo)}\nElemento menor: '{minimo}' y su posicion: {newTexto.index(minimo)}")
# Mostrar la lista con formato de texto en color blanco, una palabra al lado de la otra separada por un espacio (join).
textLista=" ".join(newTexto)
print("\nMostrar la lista con formato de texto en color blanco, una palabra al lado de la otra separada por un espacio")
print(textLista)
contMIn=ContMax=0
# Mostrar la palabra menor en rojo en cada aparición, contar cuantas apariciones tiene.
print("\nMostrar la palabra menor en rojo en cada aparición, contar cuantas apariciones tiene")
print("\nMostrar la palabra mayor en verde en cada aparición, contar cuantas apariciones tiene.\n")
for x in newTexto:
    if x == minimo:
        print(Fore.RED + x, end=" ")
        contMIn+=1
    elif x == maximo:
        print(Fore.GREEN + x,end= " ")
        ContMax+=1
    else:
        print(x,end=" ")
# Mostrar la palabra mayor en verde en cada aparición, contar cuantas apariciones tiene.
# Mostrar cuántas palabras menores y cuántas mayores se encontraron.
print("\nMostrar cuántas palabras menores y cuántas mayores se encontraron")
print(f"palabras menores {contMIn} y cuántas mayores se encontraron {ContMax}")
# print(f"\n{nuevo_texto}")