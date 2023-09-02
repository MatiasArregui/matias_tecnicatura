<<<<<<< HEAD
from os import system
system("cls")

class pruebaEncapsulamiento:
    def __init__(self, nombre, apellido, *args, **kwargs):
        self._nombre=nombre
        self._apellido=apellido
        self._args= args
        self._kwargs=kwargs
        
    @property
    def mostrarDetalle(self):
        return self._nombre
            
prueba1=pruebaEncapsulamiento("matias","arregui", 1,2,3, a="m", b="a")
print(prueba1.mostrarDetalle)
=======
class Human:
    genero="genero"
    def __init__(self, nombre, apellido, edad):
        self._nombre=nombre
        self._apellido=apellido
        self._edad=edad

    #Cambiando el valor del nombre --------------------------->
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nombre):
        self._nombre=nombre

    #Cambiando el valor del apellido --------------------------->
    @property
    def apellido(self):
        return self._apellido
    @apellido.setter
    def apellido(self, apellido):
        self._apellido=apellido

    #Cambiando el valor de genero ------------------------------->
    @classmethod
    def cambiarGenero(cls, genero:str=""):
        cls.genero=genero



persona1=Human("matias","arregui",24)
print(persona1.nombre)
persona1.nombre="nicolas matias"
print(persona1.nombre)
print(persona1.genero)
persona1.cambiarGenero("masculino")
print(persona1.genero)

>>>>>>> 3b29fca432263157d51e88ab09a5b6b05835285e
