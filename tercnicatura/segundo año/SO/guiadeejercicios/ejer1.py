# Ejercicio 1
# Escribir una función que pida un número entero entre 1 y 10 y guarde en un 
# fichero con el nombre tabla-n.txt la tabla de multiplicar de ese número, donde n es el número introducido.
while True:
    try:
        entrada=int(input("ingrese un numero del uno al diez: "))
        if entrada<1 or entrada >10:
            print("ingreso incorrecto, ingrese un numero del uno al diez")
            continue
        if 10>=entrada>=1:
            print("ingreso correcto")
            break
    except ValueError:
       print("ingrese un valor NUMERICO del uno al diez")
#Creacion de la tabla que se guardara en el fichero tabla-n.txt
tabla=""
for x in range(1,11):
    resultado=x*entrada
    tabla+=f"{x}x{entrada}= {resultado}"+"\n"
#Creacion del nombre para el fichero y su uso posterior
nombreFichero=f"tabla-{entrada}.txt"
#Se crea la carpeta
file = open(f"C:\\Users\\matiasA\\desktop\\{nombreFichero}", "w")
file.write(tabla)
file.close()