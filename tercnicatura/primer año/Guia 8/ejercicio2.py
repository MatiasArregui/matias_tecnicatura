from random import sample
from mostrarelepos import mostrarVector
from maymenpromN import minmaxprom
# Generar una lista de 30 elementos enteros al azar entre 50 y 250 inclusivos y guardarlos en un vector v1().
v1=sample(range(50,251),30)
# print(v1)
# Hacer una copia en un segundo vector v2() con los valores del primero que se encuentren entre 75 y 225.
v2=[x for x in v1 if 225 > x > 75]
# print(v1,v2)
# Crear una subrutina o procedimiento para mostrar todos los elementos de un vector cualquiera y su posición, 
# llamarla desde el main para mostrar v1 y v2.
mostrarVector("Lista v1",v1)
# print()
mostrarVector("Lista v2",v2)
# Crear una subrutina para encontrar el mayor, menor y el promedio de un vector cualquiera, 
# llamar desde el main para mostrar los resultados de v1() y v2().
minmaxprom("LISTA V1",v1)
minmaxprom("LISTA V2",v2)

