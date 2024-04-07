#Librerias a Importar
import numpy as np

from colorama import *
init(autoreset=True)
def main():
    #Encabezado
    print(Fore.BLUE+"UCAB Elaborado por: Pedro Romero ")
    print()
    #Datos de Entrada
    print(Fore.RED+"Indique numero 1 entero positivo ",end=' ') 
    n1=int(input())
    print(Fore.RED+"Indique numero 2 entero positivo distinto del numero 1",end=' ')
    n2=int(input())
    print(Fore.RED+"Indique numero 3 entero positivo distinto a los anteriores",end=' ')
    n3=int(input())

    #Procesamiento de Datos
    if(n1>n2)and(n1>n3):
        may=n1
    elif(n2>n1)and(n2>n3):
        may=n2
    else:
        may=n3
    
    #Salida de Datos
    print()
    print(Fore.BLUE+"El primer numero es",  n1)
    print(Fore.BLUE+"El segundo numero es",  n2)
    print(Fore.BLUE+"El tercer numero es",  n3)
    print(Fore.BLUE+"El Mayor numero es",  may)
main()