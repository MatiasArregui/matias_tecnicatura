from os import system
system("cls")
from colorama import init, Fore, Back, Style
init(True)
def buscador(palabra):
    for x in palabra:
        if x.upper() in palabra:
            return True
        else:
            return False
# A partir de una cadena de texto:
texto="Matias nicolas Arregui Años: 23 A cordoba"
# Mostrarlo en pantalla la cadena completa.
print(texto)
# Pasar el texto a una lista de palabras.
listaTexto=texto.split()
# Recorrer la lista con la instrucción for x in lista.
for x in listaTexto:
    # Determinar si la palabra o elemento comienza en mayúscula.
    if buscador(x):
        # Si empieza con mayúscula imprimir en color rojo
        print(f"{Back.RED} {x}")
    else:
         #sino imprimir en blanco, deben formar un párrafo.
        print(f"{Back.WHITE} {x}")





