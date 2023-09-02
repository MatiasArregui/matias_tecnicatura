# A partir de un texto:
texto1=texto=''' En un mundo fantástico y en un contexto medieval varias familias, 
    relativas a la nobleza, se disputan el poder para dominar el territorio ficticio de Poniente (Westeros) y 
    tomar el control de los Siete Reinos desde el Trono de Hierro, lugar donde el rey ejerce el poder.'''
# Mostrar en pantalla la cadena completa.
print(texto)
texto1=texto1.split()
articulos=["el", "la", "los", "las", "un", "una", "unos", "unas"]
# Imprimir nuevamente el texto pero con  los artículos (el, la, los, las, un, una, unos, unas)
#  encerrados entre asteriscos (ej: *el*)
texto3=texto[::-1]
listacomparar=texto3.split()
print(listacomparar)
# for art in texto1:
#     if art in articulos:
#         print("(" +art+")",end="")
#     else:
#         print(" " +art+ " ",end="")
# (Trabajarlo con una lista)


