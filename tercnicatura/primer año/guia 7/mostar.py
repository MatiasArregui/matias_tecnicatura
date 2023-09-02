# Crear una función para mostrar todos los elementos de un lista cualquiera y su posición, llamarla desde 
# el main para mostrar v1 y v2.
def mostrar(nombre,lista):
    print(f"Elementos de la lista: {nombre}")
    for x in lista:
        print(x,end=" ")