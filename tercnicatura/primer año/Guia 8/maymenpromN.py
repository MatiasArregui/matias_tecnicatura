# Crear una subrutina para encontrar el mayor, menor y el promedio de un vector cualquiera, 
# llamar desde el main para mostrar los resultados de v1() y v2().
def minmaxprom(nombre,lista):
    print(f"\n{nombre}\n")
    menor=min(lista)
    mayor=max(lista)
    prom= sum(lista)/len(lista)
    print(f"Mayor elemento: '{mayor}'\nMenor elemento: '{menor}'\nPromedio: {prom:.2f}")
