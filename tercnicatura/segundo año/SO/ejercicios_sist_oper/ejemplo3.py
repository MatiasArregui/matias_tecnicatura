'''
ejemplo3.py: Lee el contenido del archivo requirements.txt y localiza
la versión de Django instalada.
'''
#Biblioteca os (Operating System)
import os

#os.path.exists() devuelve True si el archivo existe.
if not os.path.exists(path='requirements.txt'):
    print('\nEl archivo no existe\n')
    quit()

#Asigna el descriptor del archivo ejemplo.txt que abre en modo read (leer)
f = open(file='requirements.txt', mode='r')

version = ''
#Lee el archivo linea por linea
for line in f:
    #Si la linea empieza con 'Django'
    if line.startswith('Django'):
        #Busca por derecha el caracter '=' y devuelve la posición.
        igual = line.rfind('=')
        #Asigna a version el texto desde la posición del caracter '=' hasta el final de la cadena
        version = line[igual + 1:]

#Si la variable version no está vacía
if version:
    print('La versión de Django es: {}'.format(version))
else:
    print('No se encontró la versión de Django')
