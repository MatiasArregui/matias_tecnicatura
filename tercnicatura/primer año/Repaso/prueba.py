texto = '''S6 fue un proyecto que comenzo dentro, de DeepMind en 2019 para acelerar para acelerar CPython 
con compilacion justo a tiempo.'''

lista1 = texto.split()
lista2 = []


lista2 = [x for x in texto if "," != x != "."]
texto1="".join(lista2)
lista2= texto1.split()
print(lista2)

lista3 = [x for x in lista2 if x.isalpha()]
print(lista3)

lista4 = [x for x in lista2 if x.isdigit()]
print(lista4)

textoNuevo = texto[::-1]
comparador = textoNuevo.split()

for x in lista3:
    if x in comparador:
        print(f"*{x}")
    else:
        print(x)

def palindromos(lista4, comparador):
    for x in lista3:
        if x in comparador:
            print(f"*{x}")
        else:
            print(x)
lista32=["juan","david","juan"]
for x in lista32:
    if x == "juan":
        lista32.remove(x)

print(lista32.count("juan"))