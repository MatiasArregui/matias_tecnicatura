# Crear una función conteo que reciba como parámetro una palabra, que diga si se encuentra en lista3, cuente y 
# muestre cuántas vocales y cuantas consonantes tiene cada elemento.
def conteo(lista,palabra):
    vocales=["a","e","i","o","u",]
    cont1=cont2=0
    palabra=palabra.lower()
    if palabra in lista:
        for x in palabra:
            if x in vocales:
                cont1+=1
            if x.isalpha() and x not in vocales:
                cont2+=1
        print(f"cantidad de vocales: {cont1} cantidad de consonantes: {cont2}")
    else:
        print("La palabra no se encuentra")

texto = 'Una cadena de bloques, conocida en inglés como blockchain, es una '\
'etiqueta que a través de una estructura de datos cuya información se agrupa '\
'en conjuntos (bloques) a los que se les añade metainformaciones relativas a '\
'otro bloque de la cadena anterior en una línea temporal para hacer un '\
'seguimiento seguro a través de grandes cálculos criptográficos. Este/ párrafo '\
'(es) para ver el- -funcionamiento *del algo-ritmo (reconocer, arenera, salas, '\
'radar, ojo, ana, ala, seres)'

# Obtener una lista de palabras a partir de texto, guardar en la lista1, a partir de lista1 crear 
# lista2 sin los caracteres de inicio y fin que no sean números ni letras, mostrar lista2.
lista1=texto.split()
lista2=[]

for x in lista1:
    juan=""
    for y in x:
        if y.isalnum():
            juan+=y
    lista2.append(juan)
print("lista 2",lista2)
juan1=["a","e","i","o","u","ú",]
# Crear lista3 con los elementos de lista2 que comienzan con vocales (utilizar sintaxis por comprensión).
lista3=[x for x in lista2 if x[0:1] in juan1]
print(lista3)
# Crear una función conteo que reciba como parámetro una palabra, que diga si se encuentra en lista3, cuente y 
# muestre cuántas vocales y cuantas consonantes tiene cada elemento.
conteo(lista3,"ana")

# Desarrollar un bloque de código para solicitar al usuario que introduzca una palabra a buscar y luego llamar 
# a la función conteo pasándole esa palabra.
while True:
    entrada=input("Ingrese la palabra a buscar:\n")
    if entrada =="":
        print("Se termino el programa")
        break
    else:
        conteo(lista1,entrada)
        conteo(lista2,entrada)
        conteo(lista3,entrada)
# Obtener una lista4 a partir de la lista3, luego aplicar a lista4 el método sort descendente, mostrar lista4.
lista4=lista3
lista4.sort(reverse=True)
print(lista4)