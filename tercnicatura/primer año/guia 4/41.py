from os import system
system("cls")
#Realizar un algoritmo para ingresar una serie de temperaturas decimales entre -20 y 50.
acum1=acum2=0
cont1=cont2=cont3=0
prom1=prom2=0

while True:
    temperaturas=float(input("Ingresar una serie de temperaturas decimales entre -20 y 50:\n"))
    
    #Salir con 100.
    if temperaturas == 100:
        break
    #Validar que los valores estén entre -20 y 50.
    if -20 > temperaturas or temperaturas > 50:
        print("Valor no admitido")
        continue
    #Contar y sacar el promedio de los valores bajo cero.
    if -20 <= temperaturas < 0:
        acum1+=temperaturas
        cont1+=1
        prom1=acum1/cont1
    #Contar y sacar el promedio de los valores sobre cero.
    if 0<temperaturas:
        acum2+=temperaturas
        cont2+=1
        prom2=acum2/cont2
    #Contar cuántos valores ingresados son iguales a cero.
    if temperaturas ==0:
        cont3+=1
    
#Mostrar resultados.
print(f"temperaturas igual a cero: {cont3}")  
print(f"temperaturas sobre cero: {cont2}\npromedio de temperatura: {prom2}")
print(f"temperaturas bajo cero: {cont1}\npromedio de temperatura: {prom1}")



