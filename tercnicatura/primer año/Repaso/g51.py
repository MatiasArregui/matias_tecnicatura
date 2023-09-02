from colorama import init, Fore,Back
init(True)
# A partir de una cadena de texto:
texto=''' Michael Thomas Edwards, Michael "Eddie" Edwards or "Eddie" Edwards (nacido en Cheltenham, 5 de diciembre de 1963),
más conocido como Eddie el Águila, es un esquiador británico que en 1988 se convirtió en el primer competidor en representar a Gran Bretaña en 
el salto de esquí olímpico desde 1929, terminando último en las pruebas de 70 m y de 90 m. Se convirtió en el poseedor del récord británico en salto 
de esquí, noveno en esquí de velocidad aficionado (171.9 km/h), así como del récord mundial de salto acrobático por saltar sobre seis autobuses.
Se hizo internacionalmente conocido por su actitud deportiva y perseverancia pese a los malos resultados obtenidos.'''
# Mostrar en pantalla la cadena completa.
print(texto)
palabrasT=[]
# Añadir una estructura de control while.
while True:
    # Solicitar al usuario ingrese una palabra a buscar en el texto.
    palabra=input("Ingrese la palabra a buscar:\n")
    # Salir con enter o sea cuando palabra sea igual ‘’
    if palabra=="":
        print("programa finalizado")
        break
    else:
        indice=0
        buscarPalabra=texto.upper().find(" "+palabra.upper()+" ",indice)
        if buscarPalabra == -1:
            # Si la búsqueda devuelve -1, mostrar el cartel “La palabra no se encuentra”
            print(f"No se encontro {palabra}")
        elif buscarPalabra !=-1:
            palabrasT.append(palabra)
            while buscarPalabra !=-1:
                # Para buscar utilizar texto.find
                buscarPalabra=texto.upper().find(" "+palabra.upper()+" ",indice)
                indice+=buscarPalabra+1
                print(f"La palabra {palabra} se encontro en la posicion: {buscarPalabra}")
                # if buscarPalabra !=-1:
                #     print(f"La palabra {palabra} se encontro en la posicion: {buscarPalabra}")
# Si la palabra se encuentra mostrar el texto con la palabra coloreada en rojo.
textoNuevo="".join(x for x in texto if x.isspace() or x.isalpha() or x.isdigit())
textVector=textoNuevo.split()
for palabra in textVector:
    if palabra.lower() in palabrasT:
        print(Back.RED + palabra + Back.RESET,end=" ")
    else:
        print(palabra,end= " ")
