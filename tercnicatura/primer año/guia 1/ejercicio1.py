from random import *
lista1=sample(range(0,101),23)
lista2=[randint(1,101) for x in range(23)]
# for x in range(23):
#     x=randint(1,101)
#     lsita
print(lista1)
print()
print(lista2)
lista3=[x for x in lista2 if x%2==0]
print(lista3)
