#el_jardín_ornamental.py
from threading import Thread

def torniquete1(cuenta):
    for i in range(0,20):
        cuenta += 1

def torniquete2(cuenta):
    for i in range(0,20):
        cuenta += 1

cuenta = 0

# Lanzar ambos procesos concurrentemente.
t1 = Thread(torniquete1(cuenta))
t2 = Thread(torniquete2(cuenta))

t1.start()
t2.start()

print("Cuenta: %d\n", cuenta)
