from colorama import Back, Fore, init
init(True)

def contProm(lista):
    cont=total=0
    for elem in lista:
        cont+=1
        total+=elem
    prom=total/cont
    print(f"Total de valores: {cont}\nPromedio de temperaturas: {prom}")



# Realizar un algoritmo para ingresar una serie de temperaturas decimales entre -20 y 50.
bajoCero=[]
sobreCero=[]
while True:
    temp=int(input("Ingrese temperaturas entre -20 y 50:\n"))
# Salir con 100.
    if temp == 100:
        print("PROGRAMA FINALIZADO\n")
        break
# Validar que los valores están entre -20 y 50.
    if -20 <= temp <= 50:
        if -20 <= temp <= 0:
            bajoCero.append(temp)
        else:
            sobreCero.append(temp)

#print(sobreCero,bajoCero)
# Contar y sacar el promedio de los valores bajo cero.
print(Fore.CYAN + "Valores bajo cero")
contProm(bajoCero)
print()
print(Fore.RED + "Valores sobre cero")
contProm(sobreCero)
# Contar y sacar el promedio de los valores sobre cero.
# Contar cuántos valores ingresados son iguales a cero.
# Mostrar resultados.
