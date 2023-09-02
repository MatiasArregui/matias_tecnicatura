def ordenador(lista):
    n=len(lista)
    for x in range(n-1):
        for y in range(n-1):
            if lista[y] > lista[y+1]:
                lista[y], lista[y+1]= lista[y+1], lista[y]

def ordenarLetras(lista):
    n=len(lista)
    for x in range(n-1):
        for y in range(n-1):
            if lista[y] > lista[y+1]:
                lista[y], lista[y+1]=lista[y+1],lista[y]
nombres=[]
# Realizar una estructura de control para permitir el ingreso de nombres.
while True:
    entrada=input("Ingrese el nombre:\n")
    # Salir con enter.
    if entrada == "":
        print("programa finalizado")
        break
    if entrada.isalpha():
        nombres.append(entrada)
nombres.count
print(nombres)
print(len(nombres))
ordenador(nombres)
# ordenarLetras(nombres)
print(nombres)
# Ordenarlos alfabéticamente sin utilizar el método sort, programar algún algoritmo de ordenamiento como burbujas, quick sort, etc.
# Al salir del bucle de carga mostrar todos los elementos.
