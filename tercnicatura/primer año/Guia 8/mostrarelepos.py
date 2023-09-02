# Crear una subrutina o procedimiento para mostrar todos los elementos de un vector cualquiera y su posición, 
# llamarla desde el main para mostrar v1 y v2.
def mostrarVector(nombre,lista):
    print(f"\n{nombre}")
    for x,y in enumerate(lista):
        print(f"Posicion: {x} Elemento: {y}")