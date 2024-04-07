import numpy as np

from colorama import *
def main():
    print(Fore.BLUE+"UCAB Elaborado por: Pedro Romero ")

    #Datos de entrada (input)
    print(Fore.BLUE+"Indique un numero de 6 digitos el cual contenga las calificaciones de sus primeros 3 notas diferentes")
    n=int(input())
    nummax=999999
    nummin=100000

    #procesamiento de datos
    
    if(n>nummax)or(n<nummin):
        print(Fore.RED+"Tu numero es incorrecto")
    else:
        resto1=n//10
        sexto_digito=n%10
        
        resto2=resto1//10
        quinto_digito=resto1%10
        
        resto3=resto2//10
        cuarto_digito=resto2%10
        
        resto4=resto3//10
        tercer_digito=resto3%10
        
        resto5=resto4//10
        segundo_digito=resto4%10
        
        resto6=resto5//10
        primer_digito=resto5%10
        
        n1=((primer_digito*10)+segundo_digito) 
        n2=((tercer_digito*10)+cuarto_digito)
        n3=((quinto_digito*10)+sexto_digito)
    print(Fore.RED+'tus notas son', n1, n2, n3)

    if(n1>20)or(n2>20)or(n3>20)or(n1<9)or(n2<9)or(n2<9):
        print("su calificacion es mayor que 20 o menor que 10 porfavor ponga la calificacion correctamente")
    else:
        mayor=float
        menor=float
        medioo=float
        #calcular todos los posibles resultados de n1
        if(n1<n2)and(n1<n3):
            menor=n1
        elif(n1>n2)and(n1>n3):
            mayor=n1
        else:
            medioo=n1

        #Calcular todos los posibles resultados de n2
        if(n2<n1)and(n2<n3):
            menor=n2
        elif(n2>n1)and(n2>n3):
            mayor=n2
        else:
            medioo=n2

        #Calcular todos los posibles resultados de n2
        if(n3<n1)and(n3<n2):
            menor=n3 
        elif(n3>n1)and(n3>n2):
            mayor=n3 
        else:
            medioo=n3
        
        mayoresnotas=((mayor+medioo)//2)
        
        #Salida de datos (output)
        print("sus calificaciones reportadas son", n)
        print("su nota menor es", menor)
        print("su nota del medio es", medioo)
        print("su nota mayor es",mayor)
        print("El promedio de sus 2 mayores notas es", mayoresnotas)
        
        
main()