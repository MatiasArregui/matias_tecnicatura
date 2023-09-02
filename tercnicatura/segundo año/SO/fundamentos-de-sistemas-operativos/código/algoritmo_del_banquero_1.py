#algoritmo_del_banquero.py
'''
La idea genérica del algoritmo es:
    1. Buscar un proceso cuya suma recAsig + recDisp >= recMax
    2. Suponemos que se asignan dichos recursos y el proceso termina su ejecución. 
       Sumamos sus recursos al vector recDisp y añadimos el proceso a la lista de finalizados.
    3. Repetir primer paso hasta terminar todos los procesos (siendo un estado estable)
       o bien hasta el punto en el que no sea posible ninguna asignación de recursos,
       existiendo pues interbloqueo.

Ejemplo:
    Proceso  |  Asignados  |  Maximos  |  Disponibles
             |  A B C D E  | A B C D E |   A B C D E   
   __________|_____________|___________|_______________  
   P0        |  1 0 2 1 1  | 1 2 2 1 2 |   0 0 2 1 1    //Recursos Disponibles Iniciales
   P1        |  2 0 1 1 0  | 2 2 2 1 0 |   1 1 3 2 1    //P3 finalizado
   P2        |  1 1 0 1 0  | 2 1 3 1 0 |   2 2 3 3 1    //P2 finalizado
   P3        |  1 1 1 1 0  | 1 1 2 2 1 |   3 2 5 4 2    //P0 finalizado
                                                        //P1 finalizado
Pasos:
 1. El primer proceso que cumple el paso 1 del algoritmo en esta tabla es P3: 
    [1 1 1 1 0]+[0 0 2 1 1] >= [1 1 2 2 1]
    Lo consideramos terminado y añadimos sus recursos a los disponibles:
    [1 1 1 1 0]+[0 0 2 1 1] = [1 1 3 2 1]
 2. Volvemos a iterar desde P0. El siguiente proceso que puede adquirir los recursos necesarios
    es P2. Añadimos sus recursos a la lista de disponibles.
 3. Ahora nos es posible terminar P0 y por último P1.
 4. Hemos logrado terminar todos los procesos sin problemas.
'''

def comprueba_configuracion(asignados, maximos, disponibles):
    finalizados = []
    i = 0
    while(i < len(asignados)):
        if not i in finalizados and puede_progresar(asignados[i], disponibles, maximos[i]):
            print('Finaliza P%s\nDisponibles: %s' % (i,disponibles))
            libera_recursos(asignados[i], disponibles)
            finalizados.append(i)   # Marca el proceso Pi como finalizado
            i = 0
        else:
            i += 1

    # Si todos los procesos finalizan
    if(len(asignados) == len(finalizados)):
        print('\nEstado seguro para la configuracion de procesos-recursos dada')
    else:
        print('\nSe produce un interbloqueo')

# Incrementamos la lista de disponibles con los que tenia asignados
def libera_recursos(asignados, disponibles):
    for i in range(len(disponibles)):
        disponibles[i] += asignados[i]

# Devuelve True si el nº de elementos asignados mas los disponibles son mayores o iguales a los
# requeridos para continuar
def puede_progresar(asignados, disponibles, maximos):
    resultado = True
    for i in range(len(maximos)):
        if(asignados[i] + disponibles[i] < maximos[i]):
            resultado = False
            break
    return resultado

asignados = [
    [1,0,2,1,1],
    [2,0,1,1,0],
    [1,1,0,1,0],
    [1,1,1,1,0]
    ]

maximos = [
    [1,2,2,1,2],
    [2,2,2,1,0],
    [2,1,3,1,0],
    [1,1,2,2,1]
    ]

disponibles = [0,0,2,1,1]
