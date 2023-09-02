from turtle import back
from colorama import init, Back, Fore,Style
init(True)

# A partir de un texto:
texto=''' En un mundo fantástico y en un contexto medieval varias familias, 
    relativas a la nobleza, se disputan el poder para dominar el territorio ficticio de Poniente (Westeros) y 
    tomar el control de los Siete Reinos desde el Trono de Hierro, lugar donde el rey ejerce el poder.'''

# Mostrar en pantalla la cadena completa.
print(texto)

# Encontrar y colorear todas las vocales en rojo.
for x in texto:
    if x.upper() == "A" :
       print(Back.RED + x,end="")
    elif x.upper() == "E":
        print(Back.RED + x, end="")
    elif x.upper() == "I":
        print(Back.RED + x,end="")
    elif x.upper() == "O":
        print(Back.RED + x,end="")
    elif x.upper() == "U":
        print(Back.RED + x, end="")
    else:
        print(x, end="")


# Para el desarrollo de este ejercicio recomiendo ir imprimiendo letra por letra dentro de un bucle for.
