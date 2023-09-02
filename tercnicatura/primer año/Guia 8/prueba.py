
def encontrar(palabra,lista):
    cont=0
    for x,y in enumerate(lista):
        if y.upper() == palabra.upper():
            print(f"La palabra: '{palabra}' esta en el texto y esta en la posicion: {x}")
            cont+=1 
    else:
        if cont ==0:
            print(f"La palabra '{palabra}' no se encuentra")
            

# A partir de una cadena de texto (no pueden ser todas mayúsculas) realizar cada punto y mostrar el resultado en pantalla.
texto2=texto='''El señor Phileas Fogg, un misterioso y solitario caballero inglés, abandonará su vida disciplinada para cumplir una apuesta 
con los miembros del Reform Club, en la que arriesgará una parte de su fortuna comprometiéndose a dar la vuelta al mundo en ochenta 
días utilizando los medios disponibles en la época.'''
# Colocar la palabra en un vector (Split).
vector=[x.lower() for x in texto]
vector="".join(vector)
vector=vector.split()
lista1=[]
lista12=""
# print(vector)
# Permitir el ingreso de una palabra para buscar en el vector (no tener en cuenta si está en mayúscula o minúsculas).
while True:
    palabra=input("Ingrese la palabra a buscar:\n")
    # Salir cuando no se ingrese ningún valor (Enter).
    if palabra == "":
        print("fin del programa")
        break
    if palabra in vector:
        # Buscar la palabra en el vector y mostrar si se encontró o no, y su posición en el vector.
        texto2=texto2.replace(" " +palabra + " "," "+palabra.upper()+" ")
        encontrar(palabra,vector)

# Unir el vector en una nueva cadena con la palabra en mayúscula y el resto como está originalmente (Join).
