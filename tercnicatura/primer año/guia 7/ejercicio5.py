def cantProm(nombre,lista):
    cant=len(lista)
    prom=sum(lista)/len(lista)
    print(f"lista: {nombre}\nCantidad: {cant}\nPromedio: {prom}\n")
from colorama import init, Back
init(True)
bajoCero=[]
sobreCero=[]
# Permitir el ingreso de una serie de temperaturas entre -60 y 60 (no debe permitir valores fuera del rango).
while True:
    temperaturas=int(input("Ingrese temperaturas entre -60 y 60:\n"))
    # Salir con 100.
    if temperaturas == 100:
        print(Back.GREEN+"\nPrograma finalizado"+Back.RESET)
        break
    if temperaturas > 60 or temperaturas < -60:
        print(Back.RED+"Entrada no Valida"+Back.RESET)
        continue
    else:
        if temperaturas < 0:
            # Obtener la cantidad y el promedio de las lecturas menores a cero grados.
            bajoCero.append(temperaturas)
        else:
            # Obtener la cantidad y el promedio de las lecturas mayores o igual a cero grados.
            sobreCero.append(temperaturas)

if len(bajoCero) > 0:
    cantProm("Bajo Cero",bajoCero)
if len(sobreCero) > 0:
    cantProm("Sobre Cero",sobreCero)
# Obtener la lectura menor y mayor de la serie.
if len(bajoCero) > 0 and len(sobreCero) > 0:
    print(f"Mayor de ambas listas:{max(sobreCero)}\nMenor de ambas listas: {min(bajoCero)}")
if len(bajoCero) > 0 and len(sobreCero) ==0:
    print(f"Mayor de ambas listas:{max(bajoCero)}\nMenor de ambas listas: {min(bajoCero)}")
if len(bajoCero) == 0 and len(sobreCero) > 0:
    print(f"Mayor de ambas listas:{max(sobreCero)}\nMenor de ambas listas: {min(sobreCero)}")