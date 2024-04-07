import colorama
from colorama import *
init(autoreset=True)
def main():
    #Entrada
    print("Indique numero entero positivo mayor que 0")
    num=int(input())
    #procesamiento
    if (num<9)or(num>99):
        print("usted a colocado un numero incorrecto por favor coloque un numero de 2 digitos")
    else:
        print("Los numeros anteriores son")
        x=0
        while(x<5):
            num-=1
            x+=1
            print(num)
    #Salida
    
main()