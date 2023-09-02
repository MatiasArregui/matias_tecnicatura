# Encontrar y mostrar el elemento menor, mayor y su posición en el vector p, inicializar menor con el primer 
# elemento del vector y mayor con nada (“”).
def minmaxpos(lista):
    menor=min(lista,key=len)
    mayor=max(lista,key=len)
    print(f"Mayor elemento: '{mayor}' Posicion: {lista.index(mayor)} \nMenor elemento: '{menor}' Posicion: {lista.index(menor)} ")
