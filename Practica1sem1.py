import numpy as np
from colorama import *
init(autoreset=True)
def main():
    #datos de entrada
    print(Fore.RED+"Ingrese su primera calificacion")
    calificacion1=int(input())
    print(Fore.RED+"Ingrese su segunda calificacion")
    calificacion2=int(input())
    print(Fore.RED+"Ingrese su tercera calificacion")
    calificacion3=int(input())

    #procesamiento
    if(calificacion1>21)or(calificacion2>21)or(calificacion3>21):
        print("Usted a Colocado un numero mayor que 20 porfavor coloque la calificacion correcta")
    else:
        resfincaf1=float(((calificacion1)*25)/100)
        
        resfincaf2=float(((calificacion2)*35)/100)
        
        resfincaf3=float(((calificacion3)*40)/100)
        
        promtotal120=int(resfincaf1+resfincaf2+resfincaf3)
        
        resporcent1=(resfincaf1*5)
        resporcent2=(resfincaf2*5)
        resporcent3=(resfincaf3*5)
        
        promtotal1100=(promtotal120*5)
        
        #datos de salida
        
        print(Fore.BLUE+"su primera calificacion es",calificacion1,Fore.BLUE+"y es equivalente a",resporcent1,"%")
        print(Fore.BLUE+"su segunda calificacion es",calificacion2, Fore.BLUE+"y es equivalente a",resporcent2,"%")
        print(Fore.BLUE+"su tercera calificacion es",calificacion3, Fore.BLUE+"y es equivalente a",resporcent3,"%")
        print(Fore.YELLOW+"su promedio total del 1 al 20 es", promtotal120)
        print(Fore.YELLOW+"su promedio total del 1 al 100 es", promtotal1100)
    
main()