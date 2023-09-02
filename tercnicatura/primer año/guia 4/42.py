from os import system
system("cls")
#De un grupo de n notas de calificación de alumnos ingresadas por teclado:
acum1=acum2=0
cont1=cont2=0
prom1=prom2=0

while True:
    notas=float(input("Ingrese una calificacion de 1 a 10:\n"))
    
    #Salir con -1.
    if notas == -1:
        break
    #Ingresar valores enteros entre 1 y 10.
    if 1>notas or notas >10:
        print("Valor erroneo")
        continue
    #Contar cuantas notas son menores a 7.
    #Sacar el promedio de notas menores a 7.
    if notas < 7:
        acum1+=notas
        cont1+=1
        prom1=acum1/cont1
    #Contar cuantas notas son mayores o iguales a 7
    #Sacar el promedio de notas mayores o iguales a 7.
    if notas >=7:
        acum2+=notas
        cont2+=1
        prom2=acum2/cont2

#Mostrar los resultados de la cantidad de notas y los promedios.
print(f"notas menores a 7: {cont1}\npromedio de notas: {prom1}")
print(f"notas iguales o mayores a 7: {cont2}\npromedio de notas: {prom2}")


