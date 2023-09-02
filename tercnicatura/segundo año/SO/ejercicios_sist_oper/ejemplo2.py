'''
ejemplo2.txt: Obtiene las carpetas especiales del sistema y
crea una carpeta sisop en el escritorio.
'''
#Biblioteca os (Operating System)
import os
from pathlib import Path
path_desktop = str(Path.home()) + '\\OneDrive\\Escritorio'
path_documents = str(Path.home()) + '\\OneDrive\\Documentos'

print(path_desktop)
print(path_documents)

lista1 = os.listdir(path_desktop)
print(lista1, '\n')

lista2 = os.listdir(path_documents)
print(lista2, '\n')

if os.path.exists(path_desktop + '\\sisop'):
    print('La carpeta ya existe no se puede continuar.')
    quit()

# Crea la carpeta sisop en el escritorio
os.mkdir(path_desktop + '\\sisop')

if os.path.exists(path_desktop + '\\sisop'):
    print('La carpeta fué creada.')
    quit()
