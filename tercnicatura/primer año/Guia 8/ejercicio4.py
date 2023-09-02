from mostrarelepos import mostrarVector
from maymenpromN import minmaxprom
# Crear un código para ingresar n valores decimales entre 1 y 100, salir con cero.
v1=[]
while True:
    entrada=int(input("Ingrese valores decimales entre 1 y 100:\n"))
    if entrada == 0:
        print("PROGRAMA FINALIZADO")
        break
    if 1<= entrada <=100:
        v1.append(entrada)
    else:
        print("INGRESO NO VALIDO")
        continue
# Guardar los valores ingresados en un vector v1() y hacer una copia en un segundo vector v2() 
# con los valores del primero que sean mayor a 50.
# v3=[x for x in v1 if x > 50 ]
v2=filter(lambda x:  x > 50,v1)
v2=list(v2)
# print(v2)
# print(f"{v2}\n{v3}")
# Crear una subrutina o procedimiento para mostrar todos los elementos de un vector cualquiera y su posición, 
# llamarla desde el main para mostrar v1 y v2.
mostrarVector("Lista V1",v1)
mostrarVector("Lista V2",v2)
# Crear una subrutina para encontrar el mayor menor y el promedio de un vector cualquiera, llamar desde el main 
# para mostrar los resultados de v1() y v2().
minmaxprom("Lista V1",v1)
minmaxprom("Lista V2",v2)
