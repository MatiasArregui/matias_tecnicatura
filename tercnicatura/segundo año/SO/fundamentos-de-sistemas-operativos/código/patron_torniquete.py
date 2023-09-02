#patron_torniquete.py
from threading import Semaphore, Thread

torniquete = Semaphore(0)
# (...)

if alguna_condicion():
    torniquete.release()
# (...)

torniquete.acquire()
torniquete.release()
