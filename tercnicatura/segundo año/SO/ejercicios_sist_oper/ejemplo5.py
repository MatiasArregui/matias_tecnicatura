'''
ejemplo5.py: Abre el archivo ejemplo.txt en modo lectura con codificación utf8.
'''
#Leyendo y escribiendo archivos con funciones built in
#Abre el archivo ejemplo.txt modo lectura con codificación utf8.
with open(file='ejemplo.txt', mode='r', encoding='utf-8') as f:
    for line in f:
        print(line, end='')

#Una vez leído el archivo, se cierra automáticamente.
#Se puede vrificar si el sierre fue exitoso con el atributo closed
f.close()
