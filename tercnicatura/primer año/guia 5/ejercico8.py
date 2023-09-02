from colorama import init, Fore,Back, Style
init(True)
# A partir de un texto:
texto=''' En un mundo fantástico y en un contexto medieval varias familias, 
relativas a la nobleza, se disputan el poder para dominar el territorio ficticio de Poniente (Westeros) y 
tomar el control de los Siete Reinos desde el Trono de Hierro, lugar donde el rey ejerce el poder.'''
texto1=texto.split()
# Mostrar en pantalla la cadena completa.
print(texto)

# Imprimir el texto y remarcar los artículos (el, la, los, las, un, una, unos, unas) en otro color.
articulos=["el", "la", "los", "las", "un", "una", "unos", "unas"]
for art in texto1:
    if art in articulos:
        print(Back.RED + art, end=" ")
    else:
        print(art,end=" ")
    
