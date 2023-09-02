'''
ejemplo4.py: Manejo
'''
import os
'''
os.popen() es una función del módulo os que se utiliza para abrir un
comando o programa externo y establecer una tubería (pipe) entre el
proceso de Python y el proceso externo.
Te permite ejecutar comandos del sistema operativo y capturar la
salida del comando en el programa de Python para su procesamiento.
La función devuelve un objeto de tipo archivo similar a lo que open()
devuelve para archivos, pero este objeto se comporta como un flujo de
lectura que contiene la salida del comando ejecutado.
Es útil cuando deseas ejecutar comandos en la línea de comandos del
sistema operativo desde tu programa Python y trabajar con su salida.
'''
#os.popen abre un proceso y devuelve un descriptor de archivo en memoria y
# a continuación el método read lo lee y asigna a la variable texto.
texto = os.popen(cmd='pip freeze').read()

#print(texto)
#Conviente la cadena en una lista de cadenas separadas por salto de línea.
lista = texto.split('\n')

for x in lista:
    #Si la cadena comienza con la palabra Django.
    if x.startswith('Django'):
        #Busca el primer gual por la izquierda y obtiene la posición.
        igual = x.find('=')
        #Obtiene la subcadena desde igual más 2 hasta el final.
        version = x[igual + 2:]
        print('La versión de Django instalada es: {}'.format(version))
        break
else:
    print('No se encontró la ninguna versión de Django instalada.')
