from colorama import init, Fore,Back,Style

# A partir de un texto:
texto=''' En un mundo fantástico y en un contexto medieval varias familias, 
relativas a la nobleza, se disputan el poder para dominar el territorio ficticio de Poniente (Westeros) y 
tomar el control de los Siete Reinos desde el Trono de Hierro, lugar donde el rey ejerce el poder.'''
# Mostrar en pantalla la cadena completa.
print(texto, "\n")
# Imprimir el texto con las vocales coloreadas según la siguiente tabla:
for letra in texto:
    if letra.upper() == "A" or letra.upper() == "Á":
        print(Fore.BLUE+letra, end="")
    elif letra.upper() == "E" or letra.upper() == "É":
        print(Fore.CYAN + letra, end="")
    elif letra.upper() == "I" or letra.upper() == "Í":
        print(Fore.GREEN + letra, end="")
    elif letra.upper() == "O" or letra.upper() == "Ó":
        print(Fore.MAGENTA + letra,end="")
    elif letra.upper() == "U" or letra.upper() == "Ú":
        print(Fore.RED + letra, end="")
    else:
        print(Fore.RESET +letra, end="")



