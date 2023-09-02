#Realizar un algoritmo que:
#Permite ingresar una serie de números enteros entre 100 y 500 inclusivos.
#Acumular los valores.
#Contar los valores.
#Sacar el promedio de los valores.
#Salir con -1.
acum1=cont1=0
while (True):
    numeros=int(input("ingrese un valor de 100 a 500 inclusivo:\n"))

    if numeros==-1:
        break

    if 500 < numeros or numeros < 100:
        print("valor incorrecto")
        continue

    if 100 <= numeros <=500:
        acum1+=numeros
        cont1+=1
        prom1=acum1/cont1
        print(f"valor correcto: {numeros}, total hasta ahora: {acum1}\npromedio: {prom1}")

print(f"promedio: {prom1}")
