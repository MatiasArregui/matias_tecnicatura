def suma(a: list,b: list =[]) -> list:
    """suma: suma dos valores enteros.

    Args:
        a (int, optional): ingresar valor. Defaults to 0.
        b (int, optional): ingresar valor. Defaults to 0.

    Returns:
        int: retorna un entero
    """
    return a+b
lista1=[1,2]
lista2=[3,4]
print(suma(lista1))
#En caso de no pasar los parametros no devuelve error, ya que en la parte de a: int =0 se le añade el valor predeterminado 0 y de esta manera 
# si el usuario devuelve un valor el 0 sera remplazado por ese valor
#si determinas el tipo de dato te ayuda a manejar la falta de argumentos