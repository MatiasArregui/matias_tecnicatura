'''
ejemplo8.py: Abre el archivo ejemplo.txt en mode binario (b) lectura (r),
luego lee el archivo y lo asigna a la variable file.
'''

file = open(file='ejemplo.txt', mode='br').read()

#Recupera cada byte del archivo en la variable byte.
for byte in file:
    #Si el byte es menor a 32, es un caracter de control.
    if byte < 32:
        print(f' 0x{byte:02x}', end=' ')
    else:
        #Si el byte es mayor o igual a 32, es un caracter imprimible.
        print(f'{byte:1c}', end='')
