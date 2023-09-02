from colorama import init,Fore,Back
# A partir de una cadena de texto:
texto=''' Michael Thomas Edwards, Michael "Eddie" Edwards or "Eddie" Edwards (nacido en Cheltenham, 5 de diciembre de 1963),
más conocido como Eddie el Águila, es un esquiador británico que en 1988 se convirtió en el primer competidor en representar a Gran Bretaña en 
el salto de esquí olímpico desde 1929, terminando último en las pruebas de 70 m y de 90 m. Se convirtió en el poseedor del récord británico en salto 
de esquí, noveno en esquí de velocidad aficionado (171.9 km/h), así como del récord mundial de salto acrobático por saltar sobre seis autobuses.
Se hizo internacionalmente conocido por su actitud deportiva y perseverancia pese a los malos resultados obtenidos.'''
# Mostrarlo en pantalla la cadena completa.
print(texto)
# Pasar el texto a una lista de palabras.
vector=texto.split()
print()
# print(vector)
# Recorrer la lista con la instrucción for palabra in lista.
for palabra in vector:
    # Determinar si la palabra o elemento comienza en mayúscula.
    if palabra[0] == palabra[0].upper() and palabra.isalpha():
        # Si empieza con mayúscula imprimir en color rojo sino imprimir en blanco, deben formar un párrafo.
        print(Back.RED + palabra + Back.RESET,end=" ")
    else:
        print(palabra,end=" ")


