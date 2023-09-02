from os import system
system("cls")
val1=val3=0
val2=val4=999

#Generar lista:
import random
#Generar una lista de 20 números enteros al azar de 3 dígitos.
for x in range(0,20):
    numeros=random.randint(100,999)
    #Encontrar el mayor entre los menores a 500.
    if 500 > numeros and val1<numeros:
        val1=numeros
    #Encontrar el menor entre los menores a 500.
    if 500 > numeros < val2:
        val2=numeros
    #Encontrar el mayor entre los mayores a 500.
    if numeros >= 500 and val3 < numeros:
        val3 = numeros
    #Encontrar el menor entre los mayores a 500.
    if 500 <= numeros < val4:
        val4 = numeros



print(f"El mayor entre los menores a 500:{val1}")
print(f"El menor entre los menores a 500:{val2}")
print(f"El mayor entre los mayores a 500:{val3}")
print(f"El menor entre los mayores a 500:{val4}")
