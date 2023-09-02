lista=[1,2,3,4,5,7]

for indice, valor in enumerate(lista):
    print(f"indice: {indice} valor: {valor}")
    
diccionario1={"value1":23, "value2":22}

for key, value in diccionario1.items():
    print(f"key: {key} value: {value}")

for key in diccionario1.keys():
    print(f"keys: {key}")
    
for value in diccionario1.values():
    print(f"value: {value}")