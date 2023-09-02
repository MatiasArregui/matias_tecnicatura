def listarNombres(*args):
    for nombre in args:
        print(f"nombre: {nombre}")

        
listaNombres=["matias", "micolas", "julian"]
# listaApellidos=["arregui", "garcia", "Romero"]
listarNombres(listaNombres) #Esto ejecuta la lista como un unico elemento CURIOSIDAD: SI PONEMOS *listaNombres, SE EJECUTA CADA ELEMENTO POR SEPARADO
# listarNombres(listaApellidos) #Esto ejecuta la lista como un unico elemento
# listarNombres("matias", "nicolas")

def listarComponentesYValores(**kwargs):
    for key, value in kwargs.items():
        print(f"Key: {key} Value: {value}")

# listarComponentesYValores(matias=24, nahuel=22)

def listarEverything(valor, *args, **kwargs):
    listarNombres(*args)
    listarComponentesYValores(**kwargs)
    print(f"Valor: {valor}")
    
listarEverything(22, "matias","nicolas","julian", m=24,a=22)

