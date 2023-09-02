# Crear una función para encontrar el mayor menor y el promedio de una lista cualquiera, 
# llamar desde el main para mostrar los resultados de v1 y v2.
def minMaxProm(lista):
    minimo=min(lista)
    mayor=max(lista)
    prom=sum(lista)/len(lista)
    return print(f"\nMayor: {mayor} Minimo: {minimo} Promedio: {prom}")