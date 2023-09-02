# Crear una función para las siguientes tareas.
# Recibir como parámetro una lista.
# Mostrar cada elemento y su posición.
# Encontrar el elemento menor y su posición por arriba del valor 50.
# Encontrar el elemento mayor y su posición por debajo del valor 50.
# Llamar a la función desde el main con dos listas diferentes de 30 y 20 valores..
from random import sample
from funcionejer7 import mostrarMayorMenor
lista30Val=sample(range(99),30)
lista20Val=sample(range(99),20)
# print(f"{lista30Val}\n{lista20Val}")
mostrarMayorMenor("Lista 30 Valores",lista30Val)
mostrarMayorMenor("Lista 20 Valores",lista20Val)