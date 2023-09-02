import os
#Cambia el nombre de una carpeta
# os.renames("C:\\Users\\matiasA\\Desktop\\carpeta de SO\\carpeta 1", "C:\\Users\\matiasA\\Desktop\\carpeta de SO\\carpeta prueba")
#-------------------------------------->
ruta=os.getcwd()
print(ruta)
#Crear un directorio (carpeta)
# os.mkdir("C:\\Users\\matiasA\\Desktop\\carpeta de SO\\carpeta ejemplo")
#Cambia el nombre de un directorio
# os.rename("C:\\Users\\matiasA\\Desktop\\carpeta de SO", "C:\\Users\\matiasA\\Desktop\\carpeta SO")
#Elimina un archivo
# os.remove("C:\\Users\\matiasA\\Desktop\\carpeta SO\\tabla-2.txt")
#eliminar un directorio
# os.rmdir("C:\\Users\\matiasA\\Desktop\\carpeta SO\\carpeta ejemplo")
# os.removedir()
#lista los directorios
directorios=" \n".join(os.listdir("C:\\Users\\matiasA\\Desktop"))
print(directorios)
