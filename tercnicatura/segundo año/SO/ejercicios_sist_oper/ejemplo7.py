'''
ejemplo7.py: Apertura y lectura de archivos con la función built in open() en mode br (binario lectura).
'''
file = open(file='ejemplo.txt', mode='br').read()
#Imprime el contenido del archivo de bytes convertidos a chr que son los caracteres de la tabla ascii.
#Se puede obserbar que todos los caracteres cuyo valor en byte es menor 32 son caracteres de control
#que no son imprimibles o visibles.
for byte in file:
    print(chr(byte), byte)
