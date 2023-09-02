from random import sample
# Inicializar 2 matrices v1 y v2 de 5 x 5 con valores enteros de hasta 2 dígitos.
v1=[]
v2=[]
def vector5x5(lista):
    for x in range(5):
        fila=[]
        for x in range(1):
            fila=sample(range(100),5)
            lista.append(fila)
def mostrarVector(lista):
    for x in range(5):
        for y in range(5):
            print(f"{lista[x][y]:>2}",end=" ")
        print()
vector5x5(v1)
vector5x5(v2)
mostrarVector(v1)
print()
mostrarVector(v2)
# Cargar las listas con números al azar con dos for anidados para filas y columnas.
# Mostrar por separado cada lista con dos for, usar print(‘{:>2}’.format(v1[f][c])).
