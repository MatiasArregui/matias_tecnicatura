from colorama import init, Back,Fore,Style
init(True)
# A partir de un texto:
texto1=texto=''''De acuerdo con Van Rossum, Python simplemente utiliza demasiada memoria y energía del 
    hardware, por lo que el no le ve futuro en la creación de sitios web, además de los servicios
    Back End y su uso en WebAssembly, explicó el portal ZDNet. «Las personas que han logrado usar 
    CPython en una tableta Android o iOS han encontrado que necesita demasiados recursos», resaltó 
    el programador.'''

# texto =''' En un mundo fantástico y en un contexto medieval varias familias, 
#     relativas a la nobleza, se disputan el poder para dominar el territorio ficticio de Poniente (Westeros) y 
#     tomar el control de los Siete Reinos desde el Trono de Hierro, lugar donde el rey ejerce el poder.'''

# Mostrar en pantalla la cadena completa.
print(texto)
# Pasar el texto a un vector v.
texto1= texto.split()
cont=0
acentos="áéíóú"
palabrasConAcentos=[]
# Contar e Imprimir nuevamente el texto coloreando las palabras con acento ortográfico.
for palabra in texto1:
    for letra in palabra:
        if letra in acentos:
            cont+=1
            print(f"{Fore.RED} {palabra}", end=" ")
            palabrasConAcentos.append(palabra)
            break
    else:
        print(f"{palabra}", end=" ")
# Mostrar el resultado del contador.
print()
print(f"Cantidad de palabras con acento: {cont}\nPalabras acentuadas: {palabrasConAcentos}")