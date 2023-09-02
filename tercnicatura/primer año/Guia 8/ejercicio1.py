from colorama import init, Fore, Back
init(True)
# from minmaxposchar import minmaxpos
# A partir de una cadena de texto iniciada en el código mostrar la cadena en color azul.
texto='''Después de la pelea contra Jiren, Goku y Vegeta vuelven a su vida habitual. Es decir, se la pasan entrenando todo el 
tiempo entre ellos para poder volverse aun más fuerte, pues Vegeta sospecha que Freezer volverá a atacarlos. Mientras tanto, 
el villano manda a sus secuaces a la Tierra para robar las esferas del dragón que Bulma tenía reunidas. #twiter %Instagram $facebook 2015 y entrenando'''
print(f"\n{Fore.BLUE} {texto}\n")
# En el texto quitar los caracteres que no sean letras ni números, mostrar nuevamente el texto en blanco, utilizar la función Replace para quitar.
# textoNuevo="".join(x for x in texto if x.isdigit() or x.isspace() or x.isalpha())
# print(textoNuevo)
for x in texto:
    if x.isdigit() or x.isspace() or x.isalpha():
        texto=texto.replace(x,x)
    else:
        texto=texto.replace(x,"")
print(f"{Fore.WHITE} {texto}")
# Convertir el texto en un vector p() de palabras y mostrar todos los elementos y su posición en blanco.
textoVcetor=texto.split()
for x,y in enumerate(textoVcetor):
    print(f"Posicion: {x} Valor: {y}")
# Encontrar y mostrar el elemento menor, mayor y su posición en el vector p, inicializar menor con el primer 
# elemento del vector y mayor con nada (“”).
# minmaxpos(textoVcetor)
min=textoVcetor[0]
max=""
for x in textoVcetor:
    if len(x) < len(min):
        min=x
    if len(x) > len(max):
        max=x
print(f"\nMayor elemento: '{max}' Posicion: {textoVcetor.index(max)} \nMenor elemento: '{min}' Posicion: {textoVcetor.index(min)} ")
# Mostrar el vector con formato de texto en color blanco, una palabra al lado de la otra separa por un espacio.
textoDelVector=" ".join(x for x in textoVcetor)
print(f"\n{Fore.WHITE}{textoDelVector}{Fore.RESET}")
# Mostrar la palabra menor en rojo en cada aparición, contar cuantas apariciones tiene.
# Mostrar la palabra mayor en verde en cada aparición, contar cuantas apariciones tiene.
# Mostrar cuántas palabras menores y cuántas mayores se encontraron.
contMin=contMax=0
for x in textoVcetor:
    if x == min:
        print(f"{Fore.RED}{x}",end=" ")
        contMin+=1
    elif x== max:
        print(f"{Fore.GREEN}{x}",end=" ")
        contMax+=1
    else:
        print(x,end=" ")
print(f"\nPalabras mayores encontradas: {contMax}\nPalbras menores: {contMin}")