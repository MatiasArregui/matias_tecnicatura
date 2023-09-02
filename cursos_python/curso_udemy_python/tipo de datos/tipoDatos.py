def comparadorTipo(dato1, dato2):
    if type(dato1) == type(dato2):
        return True
    else:
        return False

edad=24
nombre="matias"
print(type(edad))
print(type(nombre))
print(comparadorTipo(nombre,nombre))

#Entrada de datos
# entrda1=input()
while True: 
    try:
        entrada1=int(input("ingrese un valor numerico: "))
        break
    except:
        print("entrada no valida")
print(f"Entrada: {entrada1}")