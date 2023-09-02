class Perro:
    especie="perro"
    def __init__(self, nombre, raza, edad):
        self.nombre=nombre
        self.raza=raza
        self.edad=edad
    def modificarNombre(self, nombre):
        self.nombre=nombre
    def agregarAtributo(self, genero):
        self.genero= genero
    @classmethod
    def cambiarRazaClase(cls, newespecie):
        cls.especie=newespecie


perrito1=Perro("maxi", "bulldog", 22)
print(f"Nombre: {perrito1.nombre} raza: {perrito1.raza} edad: {perrito1.edad}")
perrito1.modificarNombre("tukito")
print(f"nombre nuevo: {perrito1.nombre}")
perrito1.agregarAtributo("hembra")
print(f"genero: {perrito1.genero}")
print(f"Especie: {perrito1.especie}")
perrito1.cambiarRazaClase("gato")
print(f"Especie: {perrito1.especie}")
perrito2=Perro("popis", "siames", 24)
print(f"Especie del perrito 2: {perrito2.especie}")