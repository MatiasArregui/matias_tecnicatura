# Realizar una estructura de control para permitir el ingreso de nombres.
# def ord_burbuja(arreglo):
#     n = len(arreglo)

#     for i in range(n-1):       # <-- bucle padre
#         for j in range(n-1-i): # <-- bucle hijo
#             if arreglo[j] > arreglo[j+1]:
#                 arreglo[j], arreglo[j+1] = arreglo[j+1], arreglo[j]
def ordenarLetras(lista):
    n=len(lista)
    for x in range(n-1):
        for y in range(n-1):
            if lista[y] > lista[y+1]:
                lista[y], lista[y+1]=lista[y+1],lista[y]
lista1=[]
while True:
    namae=input("Ingrese los nombres que quiera guardar:\n")
# Salir con enter.
    if namae == "":
        print("Programa finalizado")
        break
    else:
        lista1.append(namae)

# lista2=sorted(lista1) 
# print(f"{lista2}\n") 
# print(lista2)   
# Ordenarlos alfabéticamente sin utilizar el método sort, programar 
# algún algoritmo de ordenamiento como burbujas, quick sort, etc.
# Al salir del bucle de carga mostrar todos los elementos.
print(lista1)
ordenarLetras(lista1)
print(lista1)

# def ordenarLetras(lista):
#     n=len(lista)
#     for x in range(n-1):
#         for y in range(n-1-y):
#             if lista[y] > lista[y+1]:
#                 lista[y], lista[y+1]=lista[y+1],lista[y]