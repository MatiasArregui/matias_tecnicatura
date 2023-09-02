class Aritmetica:
    """
    CLASE ARITMETICA: tendra la funcionabilidad de sumar, restar, dividir, multiplicar y sacar promedio
    """
    def __init__(self, operadorA, operadorB):
        self.operadorA= operadorA
        self.operadorB= operadorB

    def suma(self):
        """
        Funcion suma
        Returns:
            int: suma de dos operadores
        """
        return self.operadorA + self.operadorB
    
    def resta(self):
        """Funcion resta
        Returns:
            int: resta de dos operadores
        """
        return self.operadorA -self.operadorB
    
    def multiplicacion(self):
        """Funcion multiplicacion

        Returns:
            int: multiplica el operador A por el operador B
        """
        return self.operadorA * self.operadorB
    
    def divicion(self)->float:
        """Funcion division

        Returns:
            float: divide el operador A por el operador B
        """
        return self.operadorA / self.operadorB
    
valor1=Aritmetica(2,3)
print(valor1.suma(),"\n")
print(valor1.resta(),"\n")
print(valor1.divicion(),"\n")
print(valor1.multiplicacion(),"\n")