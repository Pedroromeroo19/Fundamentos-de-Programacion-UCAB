import numpy as np
from colorama import *
init(autoreset=True)
def main():
    print("UCAB Elaborado por: ")
    #Variables Globales
    inicprog=0
    clvtelfarr=np.array(["2371","8215"])
    nicknamarr=np.array(["iehl","mehp"])
    #Funciones Globales
    
    #Esta Funcion tiene el objetivo de validar si el numero esta entre 1 y 6
    def Validarinicprog(y:int):
        if (y<=int(6))and(y>int(0)):
            r=True
        else:
            r=False
        return r
    
    #Esta Funcion tiene el objetivo de informar sobre el cierre del programa
    def cierreprog(x:int):
        if (x==6):
            r=True
        else:
            r=False
        return r
    
    '''Esta Funcion Tiene todos los datos de las equivalencias entre Caracter a Codigo Morce, es importante porque nos permite evaluar
    comparar una letra o caracter y al ser verificadas se devuelve el valor de una sola letra en codigo morce '''
    def DatostraductorLaCM(z:str):
        if (z=="a")or(z=="A"):
            retr=".-"
        elif (z=="b")or(z=="B"):
            retr="-..."
        elif (z=="c")or(z=="C"):
            retr="-.-."
        elif (z=="d")or(z=="D"):
            retr="-.."
        elif (z=="e")or(z=="E"):
            retr="."
        elif (z=="f")or(z=="F"):
            retr="..-."
        elif (z=="g")or(z=="G"):
            retr="--."
        elif (z=="h")or(z=="H"):
            retr="...."
        elif (z=="i")or(z=="I"):
            retr=".."
        elif (z=="j")or(z=="J"):
            retr=".---"
        elif (z=="k")or(z=="K"):
            retr="-.-"
        elif (z=="l")or(z=="L"):
            retr=".-.."
        elif (z=="m")or(z=="M"):
            retr="--"
        elif (z=="n")or(z=="N"):
            retr="-."
        elif (z=="ñ")or(z=="Ñ"):
            retr="--.--"
        elif (z=="o")or(z=="O"):
            retr="---"
        elif (z=="p")or(z=="P"):
            retr=".--."
        elif (z=="q")or(z=="Q"):
            retr="--.-"
        elif (z=="r")or(z=="R"):
            retr=".-."
        elif (z=="s")or(z=="S"):
            retr="..."
        elif (z=="t")or(z=="T"):
            retr="-"
        elif (z=="u")or(z=="U"):
            retr="..-"
        elif (z=="v")or(z=="V"):
            retr="...-"
        elif (z=="w")or(z=="W"):
            retr=".--"
        elif (z=="x")or(z=="X"):
            retr="-..-"
        elif (z=="y")or(z=="Y"):
            retr="-.--"
        elif (z=="z")or(z=="Z"):
            retr="--.."
        elif (z=="1"):
            retr=".----"
        elif (z=="2"):
            retr="..---"
        elif (z=="3"):
            retr="...--"
        elif (z=="4"):
            retr="....-"
        elif (z=="5"):
            retr="....."
        elif (z=="6"):
            retr="-...."
        elif (z=="7"):
            retr="--..."
        elif (z=="8"):
            retr="---.."
        elif (z=="9"):
            retr="----."
        elif (z=="0"):
            retr="-----"
        elif (z=="?"):
            retr="..--.."
        elif (z=="."):
            retr=".-.-.-"
        elif (z=="!"):
            retr="-.-.--"
        elif (z==","):
            retr="--..--"
        
        return retr
    
    #Esta funcion cambia una frase completa de letras a codigo morce
    def Traductor(frase:str):
        frasemorce=''
        for cont in range(0,len(frase),1):
            Letra=DatostraductorLaCM(frase[cont])
            frasemorce=frasemorce+'  '+Letra
        return frasemorce
    
    #Ciclo while para mostrar las diferentes opciones del programa
    while (inicprog != int(6)):
        #Datos de entrada
        print("")
        print(Fore.BLUE+"Porfavor indique un numero entero del 1 al 6 para indicar que desea hacer")
        print(Fore.BLUE+"Indique 1 para leer los datos de el archivo TXT(Clavtlf.txt) y almacenarlos en dos Arreglos")
        print(Fore.BLUE+"Indique 2 para mostrar los 2 Arreglo con los datos almacenados del Archivo")
        print(Fore.BLUE+"Indique 3 para codificar (Código Morse) cada uno de los Arreglos")
        print(Fore.BLUE+"Indique 4 para mostrar los Arreglos codificados (Código Morse)")
        print(Fore.BLUE+"Indique 5 para crear un Archivo (Morse.txt) con la información de los Arreglos Codificados (Código Morse)")
        print(Fore.BLUE+"Indique 6 para salir del programa")
        print("")
        
        inicprog=int(input())
        #Este condicional tiene como objetivo la validacion de los datos de entrada y el retorno de informacion
        if ((Validarinicprog(inicprog))==False):
            print(Fore.RED+"Usted a colocado un numero mayor a 6 porfavor indique un numero entre 1 y 6")
        elif ((cierreprog(inicprog))==True):
            print(Fore.GREEN+"Gracias por usar nuestro Programa, Hasta Luego!")
        else:
            #Este condicional tiene como objetivo delimitar que funcion se va a usar
            if (inicprog==1):
                print("Programa 1")
            elif (inicprog==2):
                print("Programa 2")
            elif (inicprog==3):
                '''En esta parte la funcion traductor pasa de caracter a morce cada clave/frase dentro de los arrays(clvtelfarr,nicknamarr) 
                para despues ser guardadas en un segundo array (clvtelfarrmorce, nicknamarrmorce) ya traducidos 
                el ciclo se repite con cada frase'''
                clvtelfarrmorce=np.array([str("                                     ")]*len(clvtelfarr))
                for cont in range(0,len(clvtelfarr),1):
                    clvtelfarrmorce[cont]=Traductor(clvtelfarr[cont])+" ,"
                nicknamarrmorce=np.array([str("                                     ")]*len(nicknamarr))
                for cont in range(0,len(nicknamarr),1):
                    nicknamarrmorce[cont]=Traductor(nicknamarr[cont])+" ,"
                print(Fore.GREEN+"Se ha codificado de Letras a Codigo Morce.")
            elif (inicprog==4):
                print("Entradas en clave telefono array:",*clvtelfarr)
                print("Salida clave telefono array en codigo morce",*clvtelfarrmorce)
                print("Entradas en nick name array:",*nicknamarr)
                print("Salida nick name array en codigo morce",*nicknamarrmorce)
            else:
                print("Programa 5")
main()