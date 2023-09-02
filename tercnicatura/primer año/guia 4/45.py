#Generar lista:
import random
acum1 = 0
cont1 = 0
#Generar una lista de 20 números enteros al azar de 3 dígitos.
for x in range(0,20):
    numeros = random.randint(100,999)
#Mostrar los números mayores a 300 y menores a 700 inclusivos.
    if 300 >= numeros <= 700:
        print(f"El numero mayor de 300 y menor a 700 es:{numeros}")
#Acumular los números del# rango.
        acum1 += numeros
#Contar los números del rango.
        cont1 +=1