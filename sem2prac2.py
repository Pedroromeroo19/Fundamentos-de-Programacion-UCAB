import numpy as np
from colorama import *
init(autoreset=True)
def main():
    #entrada de datos
    print("Indique numero de 4 digitos")
    numero4d=int(input())
    #procesamiento
    r1=numero4d//10
    cuartodig=numero4d%10
    r2=r1//10
    tercerdig=r1%10
    r3=r2//10
    segundodig=r2%10
    primerdig=r3%10
    
    primeros2dig=(primerdig*10+segundodig)
    ultimos2dig=(tercerdig*10+cuartodig)
    numerossum=(ultimos2dig+primeros2dig)
    numerototal=((numerossum*10000)+(ultimos2dig*100)+(primeros2dig))
    #salida de datos
    print(primerdig,segundodig,tercerdig,cuartodig)
    print(primeros2dig, ultimos2dig, numerossum)
    print(numerototal)
main()