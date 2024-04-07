import numpy as np
from colorama import *
init(autoreset=True)
def main():
    #datos de entrada
    print("Indique los km recorridos")
    distancia=int(input())
    print("Indique los minutos recorridos")
    minutos=int(input())
    #procesamiento
    veloccarro1=(distancia/minutos)
    velocporhoracaarro1=(veloccarro1*60)
    veloccarro2=((distancia/3)/minutos*3)
    #datos de salida
    print("la velocidad del carro 1 es", veloccarro1)
    print("la velocidad del carro 1 por hora es", velocporhoracaarro1)
    print("la velocidad del carro 2 es", veloccarro2)
main()