from colorama import init, Back
from mostar import mostrar
from minmaxprom import minMaxProm
# Crear un código para ingresar n valores decimales entre 1 y 100, salir con cero.
v1=[]
while True:
    entrada=int(input("Ingrese un valor entre 1 y 100 o 0 en caso de querer salir:\n"))
    if entrada==0:
        print(f"{Back.GREEN}programa finalizado{Back.RESET}")
        break
    else:
        if 1<= entrada <= 100:
            v1.append(entrada)
        else:
            print(f"{Back.RED}Valor no valido{Back.RESET}")
            continue
# print(v1)
# Guardar los valores ingresados en una lista v1 y hacer una copia en una segunda lista v2 con los valores 
# del primero que sean mayor a 50 (sintaxis por comprensión).
v2=[x for x in v1 if x > 50]
# print(v2)
# mostrar(v1)
print()
if len(v1) != 0:
    mostrar("V1",v1)
    minMaxProm(v1)
if len(v2) != 0:
    mostrar("V2",v2)
    # Crear una función para encontrar el mayor menor y el promedio de una lista cualquiera, 
    # llamar desde el main para mostrar los resultados de v1 y v2.
    minMaxProm(v2)


