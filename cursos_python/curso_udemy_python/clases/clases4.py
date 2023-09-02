from os import system
system("cls")

class FormaGeometrica:
    def __init__(self, base, altura, profundidad=0):
        self.base=base
        self.altura=altura
        self.profundidad=profundidad
 
    def obtenerArea(self)->float:
        """Funcion obtenerBase

        Returns:
            float: retorna el resutado de base * altura
        """
        return self.base * self.altura
    
    def obtenerVolumen(self)->float:
        """Funcion obtenerVolumen

        Returns:
            float: retorna el valor de la multipicacion: base * altura * superficie
        """
        return self.base * self.altura * self.profundidad
    

rectacgunlo=FormaGeometrica(12,24)
print(f"Area del rectangulo: {rectacgunlo.obtenerArea():.2f}\n")

cubo=FormaGeometrica(112,120,200)
print(f"Volumen del cubo: {cubo.obtenerVolumen():.2f}")

