'''
ejemplo6.py: Obtiene la versión de Django instalada a partir de la
ejecución del comando pip freeze
'''
#Importa la biblioteca os
import os

#os.popen abre un proceso y devuelve un descriptor de archivo en memoria
# y luego el método read() lee el archivo.
texto = os.popen(cmd='pip freeze').read()

#Obtiene la posición de la primera ocurrencia de la cadena la cual tiene
# 8 caracteres que se suman para posicionse en caracter siguiente al último igual.
desde = texto.find('Django==') + 8
#Obtiene la posición de la primera ocurrencia de la cadena la cual tiene un salto de línea \n
hasta = texto.find('\n', desde)
print(desde, hasta)
print(texto)

#Recorta la cadenha desde la posición desde hasta la posición hasta y obtiene la versión.
version = texto[desde: hasta]

print('La versión instalada de Django es: ', version)
