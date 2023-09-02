# Antes de lanzar los hilos
from threading import Semaphore
from typing_extensions import ParamSpecArgs

senal = Semaphore(0)

def envia_datos():
    calcula_datos()
    senal.acquire()
    envia_por_red()

def prepara_conexion():
    crea_conexion()
    senal.release()

def calcula_datos():
    pass

def envia_por_red():
    pass

def crea_conexion():
    pass
