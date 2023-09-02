# A partir de un texto:
texto1=texto=''' En un mundo fantástico y en un contexto medieval varias familias, 
    relativas a la nobleza, se disputan el poder para dominar el territorio ficticio de Poniente (Westeros) y 
    tomar el control de los Siete Reinos desde el Trono de Hierro, lugar donde el rey ejerce el poder.'''

# Mostrar en pantalla la cadena completa.
print(texto)
# Encontrar las vocales y reemplazarlas según la siguiente lista (a - 1, e - 2, i - 3, o - 4, u - 5)
for x in texto:
    if x.upper() == "A" :
        texto=texto.replace(x,"1")
    if x.upper() == "E":
        texto=texto.replace(x,"2")
    if x.upper() == "I":
        texto=texto.replace(x,"3")
    if x.upper() == "O":
        texto=texto.replace(x,"4")
    if x.upper() == "U":
        texto=texto.replace(x,"5")

# Mostrar como queda la nueva cadena o la cadena original modificada.
print(f"Texto original:\n{texto1}\nTexto modificado:\n{texto}")