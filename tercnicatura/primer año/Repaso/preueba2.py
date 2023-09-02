texto=" neuquen 666 234 matias"
textonuevo=""
lista1=texto.split()
for x in texto:
    if x == ".":
        continue
    else:
        textonuevo+=x
texto3=texto[::-1]
lista35=texto3.split()
lista34=texto3.split()
lista2=textonuevo.split()
lista3=[x for x in lista2 if x.isalpha()]
lista4=[x for x in lista2 if x.isdigit()]
for x in lista3:
    if x in lista35:
        print(f"*{x}")
    else:
        print(x)
for x in lista4:
    if x in lista34:
        print(f"*{x}")
    else:
        print(x)
