texto = 'Una cadena de bloques, conocida en inglés como blockchain, es una '\
'etiqueta que a través de una estructura de datos cuya información se agrupa '\
'en conjuntos (bloques) a los que se les añade metainformaciones relativas a '\
'otro bloque de la cadena anterior en una línea temporal para hacer un '\
'seguimiento seguro a través de grandes cálculos criptográficos. Este/ párrafo '\
'(es) para ver el- -funcionamiento *del algo-ritmo (reconocer, arenera, salas, '\
'radar, ojo, ana, ala, seres) neuquen 22'
def textoAlista(texto):
    lista=texto.split()
    return lista

def listaATexto(lista):
    texto=" ".join(lista)
    return texto
lista1=textoAlista(texto)
print(f"{lista1}")
texto2=listaATexto(lista1)
print(f"\n{texto2}")

def limpiaCaracteres(texto):
    lista=texto.split()
    for indice,elemento in enumerate(lista):
        if not elemento[0].isalnum():
            elemento=elemento[1:]
            lista[indice]=elemento
        if not elemento[-1].isalnum():
            elemento=elemento[:-1]
            lista[indice]=elemento
    return lista
print(limpiaCaracteres(texto))