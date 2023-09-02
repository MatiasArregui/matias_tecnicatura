# Permitir el ingreso de una serie de temperaturas entre -60 y 60 (no debe permitir valores fuera del rango).
# Salir con 100.
entradas=[]
while True:
    entrada=int(input("ingrese una serie de temperaturas entre -60 y 60:\n"))
    if entrada == 100:
        print("programa finalizado")
        break
    if entrada > 60 or entrada < -60:
        print("Valor no valido")
        continue
    else:
        entradas.append(entrada)
print(entradas)
# Obtener la cantidad y el promedio de las lecturas menores a cero grados.
ceroGrados=[x for x in entradas if x < 0]
print(f"Valores menores a cero grados: {len(ceroGrados)}\nPromedio de temperaturas: {sum(ceroGrados)/len(ceroGrados)}")
# Obtener la cantidad y el promedio de las lecturas mayores o igual a cero grados.
filtro=filter(lambda x: x>0,entradas)
sobreCero=list(filtro)
print(f"Valores menores a cero grados: {len(sobreCero)}\nPromedio de temperaturas: {sum(sobreCero)/len(sobreCero)}")
# Obtener la lectura menor y mayor de la serie.
# print(ceroGrados)
# print()
# print(sobreCero)
