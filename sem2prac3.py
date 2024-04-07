import numpy as np
from colorama import *
init(autoreset=True)
def main():
    #datos de entrada
    print("indique la cantidad de minutos que usted va a usar")
    minutos=float(input())
    #Procesamiento
    horas=float(minutos//60)
    dias=float(horas//24)
    meses=float(dias//30)
    años=float(dias//365)
    #Salida de datos
    print("Las horas son", horas, "los dias son", dias, "los meses son", meses, "los años son", años)
main()