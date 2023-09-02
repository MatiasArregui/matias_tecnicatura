'''
ejemplo1.py : Lee ejemplo.txt y añade al final una línea.

open():
-open() es una función incorporada en Python que se utiliza
para abrir archivos en modo de lectura, escritura o en otros
modos de acceso.
-Devuelve un objeto archivo que proporciona métodos para leer
o escribir en el archivo.
-Se utiliza para trabajar con archivos, no para ejecutar comandos
del sistema.
-Puedes especificar diferentes modos de apertura, como "r" para
lectura, "w" para escritura y "a" para añadir.
'''
#Asigna el descriptor del archivo ejemplo.txt que abre en modo
#append (añadir al final) codificación utf-8
descriptor = open(file='ejemplo.txt', mode='a', encoding='utf-8')

#Escribe en el descriptor al final el texto enttre comillas.
descriptor.write('\nAlumnos de Software - Segundo 2023\n')
