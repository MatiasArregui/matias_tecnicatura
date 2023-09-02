

texto=''' Michael Thomas Edwards, Michael "Eddie" Edwards or "Eddie" Edwards (nacido en Cheltenham, 5 de diciembre de 1963),
más conocido como Eddie el Águila, es un esquiador británico que en 1988 se convirtió en el primer competidor en representar a Gran Bretaña en 
el salto de esquí olímpico desde 1929, terminando último en las pruebas de 70 m y de 90 m. Se convirtió en el poseedor del récord británico en salto 
de esquí, noveno en esquí de velocidad aficionado (171.9 km/h), así como del récord mundial de salto acrobático por saltar sobre seis autobuses.
Se hizo internacionalmente conocido por su actitud deportiva y perseverancia pese a los malos resultados obtenidos.'''
# Mostrar en pantalla la cadena completa.
while True:
    palabra=input("Ingrese la palabra a buscar en el texto:\n")
    if palabra=="":
        print("Programa finalizado")
        break
    indice=0
    while True:
        buscarPalabra=texto.lower().find(" "+palabra+" ", indice)

        if buscarPalabra ==-1:
            if indice ==0:
                print("La palabra no se encuentra")
                break
            else:
                break
        else:
            print(f"La palabra {palabra} esta en la posicion {buscarPalabra}")
            indice+=buscarPalabra+1
