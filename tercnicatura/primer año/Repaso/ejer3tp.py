#practico_3.py
#A partir de un texto desarrollar el siguiente algoritmo en Python:
texto = 'neuquen 22 3305 2862 @ # $ . . . ... hola punto coma . , uno, dos. tres, '

#1 Obtener una lista de palabras a partir de texto, guardar en lista1
# y quitar los caracteres de puntuación de cada elemento de lista1
# y guardarlo en lista2.
lista1 = texto.split()
print('lista1:', lista1)

lista2 = []
#lista1 es una lista de strings o sea cada elemento es string y hay
# que tratarlo como tal.
for palabra in lista1:
    #Este for es para recorrer cada caracter de palabra.
    limpia = ''
    for caracter in palabra:
        if not caracter.isalnum():
            limpia += caracter

    lista2.append(palabra)

print('lista2:', lista2)

#2 Crear lista3 con los elementos de lista2 que no contengan números.
# (utilizar sintaxis por comprensión)
#lista3 = []
#for x in lista2:
#    if not x.isnumeric():
#        lista3.append(x)

lista3 = [x for x in lista2 if not x.isnumeric()]
print('lista3', lista3)

#3 Crear lista4 con los elementos de lista2 que no contengan alfabéticos.
# (utilizar sintaxis por comprensión)
#lista4 = []
#for x in lista2:
#    if x.isnumeric():
#        lista4.append(x)

lista4 = [x for x in lista2 if x.isnumeric()]
print('lista4', lista4)

#4 Crear una función capicuas para mostrar los elementos de lista3 y marcar
# con ‘*’ aquellos que sean capicúas.
#Alternativa uno
def capicuas1(l3):
    for x in l3:
        if x == x[::-1]:
            print('*', x)
        else:
            print(x)

#Alternativa dos
def capicuas2(l3):
    reves = ''
    for x in l3:
        reves = ''
        for y in x:
            reves = y + reves
        if x == reves:
            print('*', x)
        else:
            print(x)

print('capicúas 1')
capicuas1(lista3)
print()

print('capicúas 2')
capicuas2(lista3)
print()

#5 Crear un bucle para mostrar los elementos de lista4 y marcar con ‘*’
# aquellos que sean palíndromos.
# for x in lista4:
#     if x == x[::-1]:
#         print('*', x)
#     else:
#         print(x)
