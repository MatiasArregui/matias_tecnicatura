# Escribir una función que reciba como parámetro una cadena de palabras separadas por espacios y devuelva, como resultado, 
# cuántas palabras de más de cinco letras tiene la cadena dada.

def Contador5(texto):
    palabras=[]
    cont=0
    for x in texto:
        if x.isalnum() or x.isdigit():
            cont+=1
        if x == " " or x =="." or x == ",":
            if cont>=5:
                palabras.append(cont)
            cont=0
    return len(palabras)

texto="matias fue a pescar pero no pesco ningun pescado porque, el dique estaba bajazo."
texto2="12345678910 123 12345 1 12 123456."
palabras=[]
# for x in texto:
#     cont=0
#     if x.isalnum():
#        cont+=1
#     if cont>=5:
#         palabras.append(cont)
#     if x == " ":
#         cont=0
# conteiner=len(palabras)
# print(conteiner)
print(f"Cuantas palabras de mas de 5 letras tiene la cadena: {Contador5(texto)}")
print(f"Cuantas palabras de mas de 5 letras tiene la cadena: {Contador5(texto2)}")

