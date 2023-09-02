'''
ejempl9.py: Descarga un archivo desde el sitio indicado en url
lo graba en el disco y luego lo descomprime.
'''
# Este módulo provee una manera versátil de usar funcionalidades
# dependientes del sistema operativo.
import os
#El módulo define funciones y clases que ayudan a abrir URL (principalmente HTTP)
# en un mundo complejo: autenticación básica e implícita, redireccionamientos,
# cookies y más.
from urllib.request import urlopen

# URL del archivo.
url = 'https://sisa.msal.gov.ar/datos/descargas/covid-19/files/Covid19VacunasAgrupadas.csv.zip'
# Abre la URL URL, que puede ser una cadena o un objeto de solicitud.
r = urlopen(url)

# Nombre con el que quiero descargar el archivo.
#os.path.basename() devuelve el último componente de la ruta de un recurso.
nombre_recurso = os.path.basename(url)
print('nombre recurso:', nombre_recurso)

#Graba el archivo en el directorio actual.
with open(file=nombre_recurso, mode='wb') as f:
    f.write(r.read())
#Cierra el archivo
r.close()

'''
El módulo zipfile en Python proporciona funciones y clases para trabajar
con archivos comprimidos en formato ZIP. Te permite crear, leer y
manipular archivos ZIP, lo que puede ser útil en diversas situaciones,
como la manipulación de archivos en arreglos de datos grandes o la
organización de recursos en tus proyectos.
'''
import zipfile

password = None
# Descomprime el archivo.
# zipfile.ZipFile() abre una lista de archivos ZIP para lectura.
# archivo_zip es una lista de nombres de archivos.
archivo_zip = zipfile.ZipFile(file=nombre_recurso, mode='r')

# Intenta descomprimir el archivo.
try:
    # Imprime los archivos que contiene el archivo_zip.
    print('Archivos de la lista:', archivo_zip.namelist())
    # Extrae todos los miembros del archivo ZIP en el directorio actual.
    archivo_zip.extractall(pwd=password)
except:
    pass

# Cierra el archivo.
archivo_zip.close()

# Abre el archivo descomprimido.
with open(file=archivo_zip.namelist()[0], mode='r', encoding='utf8') as f:
    # Lee el archivo completo.
    print(f.read())
