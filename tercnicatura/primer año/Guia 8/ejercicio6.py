def encontrar(palabra,lista):
    cont=0
    for x,y in enumerate(lista):
        if y.upper() == palabra.upper():
            print(f"La palabra: '{palabra}' esta en el texto y esta en la posicion: {x}")
            cont+=1
    else:
        if cont ==0:
            print(f"La palabra '{palabra}' no se encuentra")
listar=[]
# A partir de una cadena de texto (no pueden ser todas mayúsculas) realizar cada punto y mostrar el resultado en pantalla.
texto='''El señor Phileas Fogg, un misterioso y solitario caballero inglés, abandonará su vida disciplinada para cumplir una apuesta 
con los miembros del Reform Club, en la que arriesgará una parte de su fortuna comprometiéndose a dar la vuelta al mundo en ochenta 
días utilizando los medios disponibles en la época.'''
# Colocar la palabra en un vector (Split).
textoVector=texto.split()

texto2=""
# Permitir el ingreso de una palabra para buscar en el vector (no tener en cuenta si está en mayúscula o minúsculas).
while True:
    
    entrada=input("Ingrese la palabra a buscar:\n")
# Salir cuando no se ingrese ningún valor (Enter).
    if entrada == "":
        print("Programa finalizado")
        break
    else:
        # encontrar(entrada, textoVector)
        # Buscar la palabra en el vector y mostrar si se encontró o no, y su posición en el vector.
        for x,y in enumerate(textoVector):
            cont=0
            if y.upper() == entrada.upper():
                print(f"La palabra: '{entrada}' esta en el texto y esta en la posicion: {x}")
                cont=2
                listar.append(entrada)   
        else:
            if cont == 0:
                print(f"La palabra '{entrada}' no se encuentra")
    # Unir el vector en una nueva cadena con la palabra en mayúscula y el resto como está originalmente (Join).
lista2=list(listar)
for x in textoVector:
    if x in lista2:
        texto2+="".join(" "+ x.upper())
    else:
        texto2+="".join(" "+ x)
# texto2="".join(lambda x: x in lista2
print(f"\nTexto original:\n{texto}")
print(f"\nTexto con las palabras buscadas en mayusculas:\n{texto2}")

