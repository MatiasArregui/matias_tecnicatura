from os import system
system('cls')

import threading

def torniquete1():
    contador = 0
    for i in range(0,20):
        contador += 1
        print('Hilo:', 
              threading.current_thread().getName(), 
              'con identificador:', 
              threading.current_thread().ident,
              'Contador:', contador)

def torniquete2():
    contador = 0
    for i in range(0,20):
        contador += 1
        print('Hilo:', 
              threading.current_thread().getName(), 
              'con identificador:', 
              threading.current_thread().ident,
              'Contador:', contador)

hilo1 = threading.Thread(target=torniquete1)
hilo2 = threading.Thread(target=torniquete2)

hilo1.start()
hilo2.start()
