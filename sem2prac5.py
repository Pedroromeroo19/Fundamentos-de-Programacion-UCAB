import numpy as np
from colorama import *
init(autoreset=True)
def main():
    #entrada de datos
    print("Indique la cantidad de bytes en numeros")
    b=int(input())
    #procesamiento de datos
    mb=b//1000000
    restomb=b%1000000
    kb=restomb//1000
    restokb=restomb%1000
    
    preciodisk=(kb*50)
    preciopendri=(mb*150)
    preciotot=(preciodisk+preciopendri)
    
    #salida de datos
    print("Hay",b,"bytes", ", ", mb, "megabytes y", kb, "kylobytes")
    print("usted necesita", mb,"pendrives y",kb,"Diskettes")
    print("y su precio total de los pendrive y diskettes es", preciotot)
    print("y los bytes restantes son", restokb)
main()