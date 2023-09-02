# textoNuevo="".join(letra for letra in texto if letra.isspace() or letra.isalpha() or letra.isdigit())
# vector=texto.split()
# filtro=filter(lambda letra: letra.isalpha(),vector)
# filtro=list(filtro)
# print(filtro)




#Capitalize, sirve para poner en mayuscula la primer letras
from curses.ascii import isalnum, isdigit, isspace
from re import T

from macpath import join


miCadena= "hola"
print(miCadena.capitalize())

#Count, sirve para contar cuanta veces esta un elemento en la lista
lista = [1,2,3,4,5]
cantidad = lista.count(4)
print(cantidad)
texto="David quiere ir a natura pero esta detondao"
#Find, 
while True:
    #4 Solicitar al usuario ingrese una palabra a buscar en el texto.
    palabra = input('Ingrese la palabra a buscar: ')

    #5 Salir con enter o sea cuando palabra sea igual ‘’
    if palabra == '':
        break

    i = 0
    #Esto es una variante respecto a las consignas originales ya que permite
    # encontrar todas las aparciones de la palabra mostrando en que columna se encuentra.
    while True:
        #6 Para buscar utilizar texto.find
        # Contempla casos de mayúsculas y minúsculas, utiliza la variable i para
        # relocalizar el punto a partir donde se va hacer la búsqueda.
        buscar = texto.lower().find(' ' + palabra.lower() + ' ', i)

        if buscar == -1:
            #7 Si la palabra se encuentra mostrar el texto con la palabra coloreada en rojo
            if i == 0:
                print('La palabra no se encuentra.')

            break
        else:
            #8 Si la palabra se encuentra mostrar el cartel “La palabra no se encuentra”.
            # Añade la columna donde se encuentra.
            print(Back.WHITE + Fore.RED + palabra, 'se encuentra en la columna', buscar)
            i = buscar + 1

#Index, sirve para saber el indice del elemento que buscas
print(lista.index(3)) 


#isalnum, sirve para detectar una cadena de letras y números.

cadena = int(input("Ingrese un texto: "))
print (cadena.isalnum())

#isalpha, Los métodos isalpha() devuelven "Verdadero" si todos los caracteres de la cadena son alfabetos

print(cadena.isalpha())


#isascii, Comprueba si todos los caracteres del texto son caracteres ASCII:

print(cadena.isascii())

#isdecimal, devuelve verdadero si todos los caracteres de una cadena son decimales

print(cadena.isdecimal())

#isdigit,  devuelve "Verdadero" si todos los caracteres de la cadena son dígitos.

print(cadena.isdigit())

#islower,  devuelven "Verdadero" si todos los caracteres de la cadena están en minúsculas. 

print(cadena.islower())

#isnumeric,  devuelven "Verdadero" si todos los caracteres de la cadena son numéricos. 

print(cadena.isnumeric())

#isspace, Esta función se usa para verificar si el argumento contiene todos los caracteres de espacio en blanco

print(cadena.isspace())

#isupper, devuelven "Verdadero" si todos los caracteres de la cadena están en mayúsculas

print(cadena.isupper())

#join, para convertir una lista en cadena de caracteres.

textoNuevo = " ". join(lista)

#Covertir la lista a cadena al revez:
#compresion:
textoNuevo=" ". join(x for x in reversed(lista))
textoNuevo=" ". join (lista[::-1])

for x in reversed(lista)
    textoNuevo += x+" "


#lower, Para convertir una cadena a minúsculas, utiliza el método lower()

hola = "HOLAAAAA"
minuscula = hola.lower()

#replace, sirve para remplazar un elemento por otro

texttnew= "matias arregui teke teke"
nuevaLista = texttnew.replace("matias", "david")


#split, convierte un texto a lista, sin dejar incluir los espacios

lista= texto.split()

#startswith, comprueba si la cadena empieza, por ejemplo con "Hola"

txt = "Hola, como estan"
x=txt.startswith("Hola")
print(x)

#split, Elimina los espacios al principio y al final de la cadena

texto= "   como estan    "
x= texto.split()
print(f"Hola chicos {x}, me alegro")

#translate, Reemplace cualquier carácter "S" con un carácter "P":

mydict = {83:  80}
txt = "Hello Sam!"
print(txt.translate(mydict))

#upper, Para convertir una cadena a mayúsculas

text= "hola"
mayuscula = text.upper()

#append, te agrega un elemento al final de la lista

lista.append(6)

#clear, sirve para eliminar todos los elementos de una lista

lista.clear()

#copy, sirve para copiar una lista igual a la otra

lista.copy()

#count, cuenta cuantas veces esta el elemento en la lista

print(lista.count(6))

#extend, agrega varios elementos al final de la lista
lista.extend([6,7,8])

#index, sirve para saber el indice del elemento que buscas

print(lista.index(3))

#remove, poner el valor que queremos eliminar
lista.remove(5)

#reverse, da vuelta todos los elementos

lista.reverse()

#sort, ordena los elementos ascendentemente
lista.sort()
lista.sort(reverse=True) #ordena los elementos descedientemente

#abs, calcula el valor absoluto de un número 

x = -10.76
result = abs(x)
print(result)

#chr, recibe un número y devuelve su representación como carácter

numeros = [65, 200, 66, 97, 98]
for numero in numeros:
    print("El carácter que representa a {} es {}".format(numero, chr(numero)))


#enumerate, 

lista = [1,2,3,4,5,6,7,8]

for posicion, valor in enumerate(lista):
    
    print(f"el valor {0} esta en la posicion {1}")

#filter, 
def multiple(numero):    # Primero declaramos una función condicional
    if numero % 5 == 0:  # Comprobamos si un numero es múltiple de cinco
        return True      # Sólo devolvemos True si lo es

numeros = [2, 5, 10, 23, 50, 33]

filter(multiple, numeros)

#len, sirve para calcular cuantos elementos tiene una lista

print(len(lista))

