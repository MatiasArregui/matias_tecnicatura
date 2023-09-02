import threading

def worker():
    #'''funcion que realiza el trabajo en el thread'''
    print('Estoy trabajando para Genbeta Dev')
    return

threads = list()

for i in range(3):
    t = threading.Thread(target = worker)
    threads.append(t)
    t.start()

#print(threads)
