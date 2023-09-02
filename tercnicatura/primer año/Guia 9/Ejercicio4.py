# Escriba un programa que permita crear una lista de palabras y que, 
# a continuación, pida una palabra y diga cuántas veces aparece esa palabra en la lista.
lista=[]
while True:
    entrada=input("ingrese una palabra para agregar a la lista o salir para cerrar el programa:\n")
    if entrada.lower() == "salir":
        print("Progama finalizado")
        break
    else:
        lista.append(entrada.lower())
        print("¿Quiere saber cuantas veces esta una palabra en la lista? Y/N")
        q=input()
        if q.lower() == "y":
            palabra=input("ingrese la palabra a buscar:\n")
            print(lista.count(palabra.lower()))
        if q.lower() != "y" and q.lower()!="n":
            print("valor no valido")
            continue 
print(f"Lista: {lista}")