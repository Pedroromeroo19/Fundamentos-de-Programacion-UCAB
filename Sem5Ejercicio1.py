def main():
    #entrada de datos
    print("UCAB Elaborado por Pedro Romero")
    print()
    print("Indique la jugada del Jugador 1 (pulse 1 para pare o 2 para none)")
    jg1=int(input())
    if(jg1==1):
        j2=2
    else:
        j2=1
    print("indique numero del jugador 1 (1-5)")
    n1=int(input())
    print("indique numero del jugador 2 (1-5)")
    n2=int(input())
    #Procesamiento de datos
    r= (n1+n2)
    x=(r%2)
    if(x==0):
        if (jg1==1):
            g="jugador 1"
        else:
            g="jugador 2"
    else:
        if(jg1==1):
            g="jugador 2"
        else:
            g="jugador 1"
    
    #Salida de datos
    print("La jugada del jugador 1 es:", jg1)
    print("El numero del jugador 1 es:", n1)
    print("La jugada del jugador 2 es:", jg1)
    print("El numero del jugador 2 es:", n2)
    print("jugada 1 pares, Jugada 2 nones")
    print("La suma del numero es", r)
    print("el ganador del juego es: ", g)
main()