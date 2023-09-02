from random import sample, randint

def mostarVector(lista):
    n=len(lista)
    for x in range(n):
        for y in range(n):
            print(f"{lista[x][y]:>2}",end=" ")
        print()

def printVector(lista):
    for x in range(5):
        for y in range(5):
            # print("{:>2}".format(lista[x][y]),end=" ")
            print(f"{lista[x][y]:>2}",end=" ")
        print()
def vectoriZador(lista):
    for x in range(5):
        fila=[]
        for y in range(5):
            elem=randint(0,100)
            fila.append(elem)
        lista.append(fila)
        
v1=[]
vectoriZador(v1)
# vector5x5(v1)
mostarVector(v1)
