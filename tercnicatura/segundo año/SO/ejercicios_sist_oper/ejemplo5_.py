#with open(file='ejemplo.txt', mode='r', encoding='utf-8') as f:

#Uso de la función built in open() sin la cláusula with, abre el
# archivo ejemplo.txt modo lectura con codificación utf8.
f = open(file='ejemplo.txt', mode='r', encoding='utf-8')

for line in f:
    print(line, end='')

f.close()
