from os import system
system("cls")
cadena="matias se fue a buscar a nahuel al trabajo"

lista=[x.capitalize() for x in cadena.split()]
print(cadena.startswith("s",7))
print(cadena.strip("m"))
# print(lista)
# print(cadena)
texto = ' hola mundo hola \ni'
print(texto.strip(' oahl'))
texto2= ' holai mundo hola \ni'
print(texto2.strip(' \nihloand'))
print(texto2.lstrip(' \nihloand'))
print(texto2.rstrip(' \nihloand'))
