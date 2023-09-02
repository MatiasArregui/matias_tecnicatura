# A partir de un texto:
texto=''' La historia presenta a un narrador anónimo obsesionado con el ojo enfermo (que llama "ojo de buitre") 
de un anciano con el cual convive. Finalmente decide asesinarlo. El crimen es estudiado cuidadosamente y, 
tras ser perpetrado, el cadáver es despedazado y escondido bajo las tablas del suelo de la casa. La policía 
acude a la misma y el asesino acaba delatándose a sí mismo, imaginando alucinadamente que el corazón del viejo 
se ha puesto a latir bajo la tarima. 
'''
# Mostrar en pantalla la cadena completa.
print(texto)
# Pasar el texto a un vector de palabras.
texto1=texto.split()
letras=["a","á","e","é","i","í","o","ó","u","ú"]

for x,y in enumerate(texto1):
    print(x,y)
    print(y[0:1])
    if y[0:1].lower() in letras:
        texto1[x]="(" + y + ")"
texto1= " ".join(texto1)
print(texto1)
# Recorrer el vector y encerrar entre paréntesis aquellas palabras que empiecen con una vocal 
# minúsculas, mayúscula o acentuada.
# Armar o concatenar el vector en otra variable String como por ejemplo nuevotexto.
# Imprimir el nuevo texto.