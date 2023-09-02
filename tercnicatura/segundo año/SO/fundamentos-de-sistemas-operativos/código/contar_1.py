'''
Dos hilos que llaman la función contar que utiliza la variable contador.
Cuenta hasta 100.
'''
import threading

def contar():
    '''Contar hasta cien'''
    contador = 0

    while contador < 100:
        contador += 1
        print('Hilo:', 
              threading.current_thread().getName(), 
              'con identificador:', 
              threading.current_thread().ident,
              'Contador:', contador)

hilo1 = threading.Thread(target = contar)
hilo2 = threading.Thread(target = contar)

hilo1.start()
hilo2.start()
