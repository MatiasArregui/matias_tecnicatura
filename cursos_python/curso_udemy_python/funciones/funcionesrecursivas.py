def factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero-1)
    
print(factorial(5))

def descendente(numero):
    if numero>=1:
        print(numero)
        descendente(numero-1)
    elif numero==0:
        return print(numero)
    elif numero <=0:
        print("valor incorrecto...")

descendente(5)