import random
from colorama import init, Fore, Back
init(True)
def printVector(lista):
    for x in range(5):
        for y in range(5):
            # print("{:>2}".format(lista[x][y]),end=" ")
            print(f"{lista[x][y]:>2}",end=" ")
        print()



def vectorizador(lista):
    for x in range(5):
        newlist=random.sample(range(0,99), 5)
        lista.append(newlist)
# Inicializar 2 matrices v1 y v2 de 5 x 5 con valores enteros de hasta 2 dígitos.
v1=[]
vectorizador(v1)
#print(v1)
# print(v1[1][1])
v2=[]
vectorizador(v2)
#print("{:>2}".format(v1[1][2],end=""))
# print(v2)
# Cargar las listas con números al azar con dos for anidados para filas y columnas.
# Mostrar por separado cada lista con dos for, usar print(‘{:>2}’.format(v1[f][c]))
print(Back.RED + "Vector1\n" + Back.RESET)
printVector(v1)
print()
print(Back.GREEN + "vector2\n" + Back.RESET)
printVector(v2) 
 

# for x in range(5):
#     for y in range(5):
#         print('{:>2}'.format(v1[x][y]), end=' ')
#     print()