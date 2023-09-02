from minmaxposchar import minmaxpos
from mostrarVector import mostrarVector
# A partir de una cadena de texto texto1 inicializada en el código, convertir en un vector p() de palabras y mostrar.
texto1='''Es una serie Manga que cuenta la historia de un joven ninja hiperactivo llamado Naruto Uzumaki que hará todo lo 
posible por ascender al máximo grado ninja de su aldea con el propósito de ser reconocido como alguien importante dentro de su aldea.'''
textoVector=texto1.split()
print(f"Texto a Vector:\n{textoVector}")
# Mostrar el elemento menor (en cantidad de caracteres), mayor (en cantidad de caracteres) y su posición del vector p().
print()
minmaxpos(textoVector)
# Concatenar los elementos en una nueva cadena texto2 pero en sentido inverso, es decir donde el primer elemento sea el 
# último elemento de p() y mostrar al finalizar.
# texto2=" ".join(textoVector[::-1])
texto2=" ".join([x for  x in reversed(textoVector)])
print(f"\nTexto al inverso\n{texto2}\n")
# Crear un procedimiento para mostrar el vector p(), llamar desde main.
mostrarVector("Texto Vectorizado",textoVector)
print()