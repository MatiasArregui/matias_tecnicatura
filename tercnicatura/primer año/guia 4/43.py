
#Generar lista
import random
#Generar una lista de 20 números enteros al azar de 3 dígitos.
for x in range(0,20):
    numeros=random.randint(100,999)
    #Mostrar toda lista.
    print(f"vuelta {x} numero {numeros}")
    #Marcar con * (asterisco) los divisibles por 2.
    if numeros%2==0:
        print(f"*{numeros}")
    #Marcar con # (numeral) los divisibles por 3.
    if numeros %3 ==0:
        print(f"#{numeros}")
    #Marcar con $ (peso) los divisible por 4.
    if numeros %4 ==0:
        print(f"$ {numeros}")
    #Marcar con & (per se and per sand – por sí mismo) los divisibles por 5.
    if numeros %5 ==0:
        print(f"& {numeros}")

