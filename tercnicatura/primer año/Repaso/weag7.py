# Crear una función para mostrar todos los elementos de un lista cualquiera y su posición, llamarla desde 
# el main para mostrar v1 y v2.



def mostarElementos(nombre,lista):
    print(f"LISTA: {nombre}\n")
    for x,y in enumerate(lista):
        print(f"Posicion: {x} Elemento: {y}")
    print()
# Crear una función para encontrar el mayor menor y el promedio de una lista cualquiera, llamar desde el 
# main para mostrar los resultados de v1 y v2.
def minMaxProm(nombre,lista):
    print(f"LISTA: {nombre}\n")
    minimo=min(lista)
    maximo=max(lista)
    prom=sum(lista)/ len(lista)
    print(f"Mayor: {maximo}\nMenor: {minimo}\nPromedio: {prom}")
    print()



# Crear un código para ingresar n valores decimales entre 1 y 100, salir con cero.
v1=[]
while True:
    entrada=int(input("Ingrese un valor entre 1 y 100 o 0 en caso de querer salir:\n"))
    if entrada==200:
        print("PROGRAMA FINALIZADO")
        break
    if 100<entrada or entrada <1:
        print("Valor no valido")
        continue
    else:
        v1.append(entrada)


# Guardar los valores ingresados en una lista v1 y hacer una copia en una segunda lista v2 con los valores 
# del primero que sean mayor a 50 (sintaxis por comprensión).
v2=[x for x in v1 if x>50]

if len(v1) > 0:
    mostarElementos("LISTA V1",v1)
    minMaxProm("LISTA V1",v1)
if len(v2) > 0:
    mostarElementos("LISTA V2",v2)
    minMaxProm("LISTA V2",v2)


