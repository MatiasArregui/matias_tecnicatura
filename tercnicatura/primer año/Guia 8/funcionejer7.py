# Crear una función para las siguientes tareas.
# Recibir como parámetro una lista.
# Mostrar cada elemento y su posición.
# Encontrar el elemento menor y su posición por arriba del valor 50.
# Encontrar el elemento mayor y su posición por debajo del valor 50.
# Llamar a la función desde el main con dos listas diferentes de 30 y 20 valores..
def mostrarMayorMenor(nombre,lista):
    print(nombre)
    listaUp50=[]
    listaLow50=[]
    for indice,elem in enumerate(lista):
        print(f"Elemento: {elem} Posicion: {indice}")
        if elem < 50:
            listaLow50.append(elem)
        else:
            listaUp50.append(elem)
    # Encontrar el elemento menor y su posición por arriba del valor 50.
    miniU50=min(listaUp50)
    # Encontrar el elemento mayor y su posición por debajo del valor 50.
    maxL50=max(listaLow50)
    print(f"Elemento menor: {miniU50} y su posición: {lista.index(miniU50)} por arriba del valor 50")
    print(f"Elemento mayor: {maxL50} y su posición: {lista.index(maxL50)} por debajo del valor 50")
