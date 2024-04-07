import numpy as np
from colorama import *
init(autoreset=True)
def main():
    #datos de entrada
    print("Indique numero de 6 digitos")
    N=int(input())
    print("Indique numero de un digitos indicando D")
    D=int(input())
    print("Indique numero de un digitos indicando M")
    M=int(input())
    #validez
    if(N>999999)or(N<100000)or(D>9)or(D<1)or(M>9)or(M<1):
        print("El numero que puso es incorrecto")
    else:
    #procesamiento
        resto1=N//10
        sextdig=N%10
        resto2=resto1//10
        quintdig=resto1%10
        resto3=resto2//10
        cuartdig=resto2%10
        resto4=resto3//10
        tercedig=resto3%10
        resto5=resto4//10
        segundig=resto4%10
        primerdig=resto5%10
        
        primergrupo=((primerdig*10)+segundig)
        grupomedio=((tercedig*10)+cuartdig)
        grupofinal=((quintdig*10)+sextdig)
        
        invprimergrup=((segundig*10)+primerdig)
        invgrupomedio=((cuartdig*10)+tercedig)
        invgrupofinal=((sextdig*10)+quintdig)
        
        P=((invgrupofinal*10000)+(invgrupomedio*100)+invprimergrup)
        R=((invgrupofinal*1000000)+(D*100000)+(invgrupomedio*1000)+(M*100)+invprimergrup)
        
    #Salida de datos
        print("estos son tus digitos", primerdig,segundig, tercedig, cuartdig, quintdig, sextdig)
        print("estos son tus digitos agrupados", primergrupo, grupomedio, grupofinal)
        print("estos son el inverso de tus digitos agrupados", invprimergrup, invgrupomedio, invgrupofinal)
        print("el numero obtenido es", R)
        print("El numero inverso es", P)
main()