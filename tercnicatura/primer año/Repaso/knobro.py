# lista=["mateo","juan","david","matias"]
# print(lista)
# lista.pop(lista.index("juan"))
# print(lista)
# texto="encara pa la villa con un termidor"
# # texto=texto.replace("encara ","")
# # print(texto)
def buscar(texto):
    while True:
        entrada=input("ingrese la palabra a buscar:\n").lower()
        if entrada == "":
            print("nos re vimo")
            break
        else:
            indice=0
            # final=6
            while True:
                buscarPalabra=texto.lower().find(""+entrada+"",indice)
                #find(palabra,comienzo,final)
                #count(palbra,inicio,final)
                if indice== 0 and buscarPalabra ==-1:
                    print("la palabra no se encuentra")
                    break
                if buscarPalabra !=-1:
                    print(f"La palabra esta en la posicion: {buscarPalabra}")
                    indice+=buscarPalabra+1
# def limpiador1(texto):
#     lista=texto.split()
#     for indice,palabra in enumerate(lista):
#         if not palabra[0].isalnum(): 
#             lista[indice]=palabra[1:]
#         if not palabra[-1].isalnum():
#             lista[indice]=palabra[:-1]
#     return lista
def limpiadorDeTexto(texto):
    lista=texto.split()
    for indice,palabra in enumerate(lista):
        



texto="matias #fue a /una conve=ncion anime- y, se -perdio$"
# buscar(texto)
# texto=limpiador1(texto)
# print(limpiador1(texto))
# lista1=["matias","nicolas","arregui"]
# print(limpiador1(texto))
