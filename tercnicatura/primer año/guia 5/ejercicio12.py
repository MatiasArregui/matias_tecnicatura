#Guía 5 - Ejercicio 12.py
from colorama import init, Fore
init(True)

#1 A partir de un texto
texto = 'De acuerdo con Van Rossum, Python simplemente utiliza demasiada memoria y energía del ' \
    'hardware, por lo que el no le ve futuro en la creación de sitios web, además de los servicios ' \
    'Back End y su uso en WebAssembly, explicó el portal ZDNet. «Las personas que han logrado usar ' \
    'CPython en una tableta Android o iOS han encontrado que necesita demasiados recursos», resaltó ' \
    'el programador.'

#2 Mostrar en pantalla la cadena completa.
print()
print(texto)
print()

#3 Pasar el texto a un vector v.
v = texto.split()
print(v)
print()

#4 Contar e imprimir nuevamente el texto coloreando las palabras
# con acento ortográfico.
contar=0
acentos='áéíóú'

for palabra in v:
    flag=False

    for letra in palabra:
        if letra.lower() in acentos:
            contar += 1
            flag=True
            break

    if flag:
        print(Fore.RED + palabra, end=' ' )
    else:
        print(palabra, end=' ')

#5 Mostrar el resultado del contador.
print()
print('Cantidad de palabras con acento ortográfico', contar)