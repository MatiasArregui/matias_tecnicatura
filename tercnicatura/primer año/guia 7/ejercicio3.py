from colorama import Back, init,Fore
init(True)

# A partir de una cadena de texto inicializada en el código, convertir a una lista p de palabras y mostrar.
texto='''En un mundo fantástico y en un contexto medieval varias familias, relativas a la nobleza, 
se disputan el poder para dominar el territorio ficticio de Poniente (Westeros) y tomar el control de los Siete Reinos 
desde el Trono de Hierro, lugar donde el rey ejerce el poder.'''
print(f"Texto Original:\n{texto}")
lisText=texto.split()
# Mostrar el elemento menor (en cantidad de caracteres), mayor (en cantidad de caracteres) y 
# su posición en la lista p (aplicar min y max con el parámetro key = len)
menor=min(lisText,key=len)
mayor=max(lisText,key=len)
# posicionMin=[x for x in lisText if x == menor]
posMin=[x for x, y in enumerate(lisText) if y == menor]
posMayor=[x for x,y in enumerate(lisText) if y == mayor]
# print(posicionMin)
# ejemplo: menor = min(palabras, key = len).
print(f"\n{Back.CYAN}{Fore.BLACK}Mostrar el elemento menor: {menor}, mayor: {mayor} y su posición en la lista: Mayor: {lisText.index(mayor)} Menor: {lisText.index(menor)}{Back.RESET}{Back.LIGHTGREEN_EX}\nMenor todas las posiciones ocupadas en lista: {posMin} mayor todas las posiciones ocupadas en lista: {posMayor}")
# Concatenar los elementos de la lista en una nueva cadena nuevo_texto pero en sentido inverso, es decir donde el 
# primer elemento sea el último elemento de p y mostrar al finalizar (aplicar join con for reversed).
listaReversa=" ".join(lisText[::-1])
print(f"\n{Back.GREEN}Texto en reversa forma uno:{Back.RESET}")
print(listaReversa)
listaReversa2=" ".join(x for x in reversed(lisText))
print(F"\n{Back.RED}Texto en reversa forma dos:{Back.RESET}")
print(listaReversa2)
print()
# Crear una función para mostrar la lista p, llamar desde main.
