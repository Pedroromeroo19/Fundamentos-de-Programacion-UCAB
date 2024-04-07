import numpy as np
from colorama import *
init(autoreset=True)

def main():
    
    #VARIABLES GLOBALES
    
    #Valor introducido por el usuario en el menu principal
    inicprog=0
    #Arreglo de las claves telefonicas en texto
    clavtxt: np.array
    #Arreglo de los nicknames en texto
    nametxt: np.array
    #Arreglo de las claves telefonicas en código morse
    clavcod : np.array
    #Arreglo de los nicknames en código morse
    namecod: np.array
    
    #FUNCIONES:
    
    #Validar si el valor introducido por el usuario corresponde a un numero real
    def Validarnum(w: str):
        r = True 
        for i in range (0, len(w), 1):
            if (ord(w[i]) < 48) or (ord(w[i]) > 57):
                r = False
        return r
    
    #Indicar cual fue el error cometido por el usuario al introducir un número incorrecto en la interfaz principal
    def Errorinic(x:int):
        print("")
        if (x>6):
            print(Fore.RED+"ERROR:", " el número indicado es mayor que 6, por favor intente nuevamente.")  
        else:
            print(Fore.RED+"ERROR:", " el número indicado es menor que 1, por favor intente nuevamente.")
        print("")
        print("")
    #Indicar cual fue el error cometido por el usuario al introducir un número incorrecto en las funciones 2 y 4.
    def Error1y4(y:int):
        if (y>4):
            print(Fore.RED+"ERROR:", " el número indicado es mayor que 4, por favor intente nuevamente.")  
        else:
            print(Fore.RED+"ERROR:", " el número indicado es menor que 1, por favor intente nuevamente.")
        print("")
        
    
    #Codificar a morse una letra o número perteneciente a un nickname o clave telefónica
    '''Esta Funcion Tiene todos los datos de las equivalencias de caracter a codigo Morce, es importante ya que permite 
       devolver el valor de una letra o número en código morse. Esto se logra al comparar dicha letra o número  con cada 
       uno de los caracteres presentes en el condicional y así asignarle el valor correspondiente '''   
    def Codificmorse(z:str):
        retr = "."
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
    
    #Cambiar una frase de letras o números (correspondientes a los nicknames y claves telefónicas) de texto a código morse
    def Traductor(frase:str):
        frasemorse=''
        # Ciclo 'para' con la finalidad de extraer cada letra del nickname o clave telefonica en texto para despues codificarla y concatenarla con la frase morse
        for i in range(0,len(frase),1):
            #Se llama el metodo Codificmorse, cuyo parámetro corresponde a un caracter en particular del nickname o clave telefonica  tratada en el momento 
            Letra=Codificmorse(frase[i])
            frasemorse += (Letra +' ')
        #Se devuelve el nickname o clave telefonica ya codificada, contenida en la variable frasemorse
        return frasemorse
    
    
    #PROCEDIMIENTOS: 
    
    #Crear dos arreglos (uno con los nicknames y otro con las claves telefónicas) a partir del archivo Clavtlf.txt
    def Textoarr ():
        nonlocal clavtxt, nametxt
        arch = open(r"C:\\Users\\Pedro\\OneDrive\\Desktop\\Estudios Ucab\\Semestre 1\\Fundamentos de Programacion\\Semana 15 FP\\Proyectoprueban1.0.0.txt", "rt")
        cont= 0
        for linea in arch.readlines():
            cont +=1
        arch.close()
        clavtxt = np.array(["    "]*int(cont/2))
        nametxt = np.array(["    "]*int(cont/2)) 
        i=0
        arch= open(r"C:\\Users\\Pedro\\OneDrive\\Desktop\\Estudios Ucab\\Semestre 1\\Fundamentos de Programacion\\Semana 15 FP\\Proyectoprueban1.0.0.txt", "rt")
        for linea in arch.readlines():
            if (ord(linea[1]) >= 48) and (ord(linea[1])<= 57):
                clavtxt[i]= linea
            else:
                nametxt[i]= linea
                i += 1 
        arch.close()
        
        print("")
        print (Fore.CYAN+"Se han creado los arreglos de los nicknames y de las claves telefonicas de los usuarios satisfactoriamente")
        print("")
        print("")
    
    #Desplegar los datos almacenados en los arreglos de los nicknames y de las claves telefonicas (funciona para los arreglos en texto y los arreglos en código morse)
    def Printarreglos(n: np.array, c: np.array, tex1: str, tex2: str, tex3: str, tex4: str):
        print("")  
        print("Introduzca", Fore.BLUE+"'1'", "si desea desplegar  los nicknames", tex1,  "de los usuarios")
        print("Introduzca", Fore.BLUE+"'2'", "si desea desplegar  las claves telefonicas", tex2, "de los usuarios ")
        print("Introduzca", Fore.BLUE+"'3'", "si desea desplegar los nicknames y claves telefonicas", tex2, "de cada usuario")
        print("Introduzca", Fore.BLUE+"'4'", "si desea regresar al menu principal")
        mod = input()
        print("")
        if (Validarnum(mod)==False):
            #El valor introducido por el usuario no corresponde a un número real
            print(Fore.RED+"ERROR:", " El valor introducido no corresponde a un numero entero positivo, por favor intente nuevamente.")
            print("")
            if(int(inicprog)==2):
                Printarreglos(nametxt, clavtxt," "," "," "," ")
            else:
                Printarreglos(namecod, clavcod," codificados ", " codificadas ", " codificado ", " codificada ")
        elif (int(mod) < 1) or (int(mod) > 4): 
            Error1y4(int(mod))
            if(int(inicprog)==2):
                Printarreglos(nametxt, clavtxt," "," "," "," ")
            else:
                Printarreglos(namecod, clavcod," codificados ", " codificadas ", " codificado ", " codificada ")
        elif (int(mod) == 1):
            for i in range (0,len(n), 1):
                j = 0
                j = (i + 1)
                print ("El nickname", tex3, "del cliente", j, " es: ", end=' ')
                print(Fore.BLUE+n[i])
            print("")
            print("")
        elif (int(mod) == 2):
            for i in range (0,len(c), 1):
                j = 0
                j = (i + 1)
                print ("La clave telefonica", tex4, "del cliente", j, " es: ", end=' ')
                print(Fore.BLUE+c[i])
            print("")
            print("")  
        elif (int(mod)== 3):
            for i in range (0,len(c), 1):
                j = 0
                j = (i + 1)
                print ("El nickname", tex3, "del cliente", j, " es: ", end=' ')
                print(Fore.BLUE+n[i])
                print ("La clave telefonica", tex4, "del cliente", j, " es: ", end=' ')
                print(Fore.BLUE+c[i])
                print("")
            print("")  
        else:
            print (Fore.CYAN+"Regresando al menu principal")
            print("")
            print("")
            
    def ArchMorse(c: np.array, n: np.array):
            arch = open(r"C:\\Users\\Pedro\\OneDrive\\Desktop\\Estudios Ucab\\Semestre 1\\Fundamentos de Programacion\\Semana 15 FP\\archmorse1.0.1.txt","wt")
        
            for i in range(0,len(c),1):
                y=str(c[i])
                x=str(n[i])
                arch.write(y)
                arch.write("\n") 
                arch.write(x)
                arch.write("\n")     
            arch.close()
                    
    #ENCABEZADO
    
    print(Fore.YELLOW + """

█   █  █████  █████  ████  
█   █  █      █   █  █   █ 
█   █  █      █████  █ █ 
█   █  █      █   █  █   █ 
█   █  █      █   █  █   █ 
█████  █████  █   █  █████  
""")
    
    
    print(Fore.GREEN + "Elaborado por: ")
    print(Fore.WHITE)
    print("Luis Morales (30.885.952)")
    print("Matias Leon (30.849.345)")
    print("Gabriel López (30.821.466)")
    print("Pedro Romero (30.712.435)")
    print()
    
    #CICLO MIENTRAS PARA MOSTRAR LAS DIFERENTES OPCIONES DEL PROGRAMA
    
    #El programa finaliza cuando el valor introducido por el usuario es igual a 6, pues de esta forma la condición del ciclo mientras no se cumple y por tanto se llega al final del programa
    while (inicprog != "6"):
        print(Fore.BLUE+"Porfavor introduzca un numero entero positivo del 1 al 6 para indicar cual función se desea realizar")
        print("")
        print("Introduzca", Fore.BLUE+"'1'"," para leer los datos de el archivo TXT(Clavtlf.txt) y almacenarlos en dos Arreglos")
        print("Introduzca", Fore.BLUE+"'2'"," para mostrar los  Arreglos con los datos almacenados del Archivo")
        print("Introduzca", Fore.BLUE+"'3'"," para codificar (Código Morse) cada uno de los Arreglos")
        print("Introduzca", Fore.BLUE+"'4'"," para mostrar los Arreglos codificados (Código Morse)")
        print("Introduzca", Fore.BLUE+"'5'"," para crear un Archivo (Morse.txt) con la información de los Arreglos Codificados (Código Morse)")
        print("Introduzca", Fore.BLUE+"'6'"," para salir del programa")
        
        # Se obtiene el numero indicado por el usuario para determinar cual funcion se desa realizar
        inicprog=input()
        
        #Este condicional tiene como objetivo la validacion de los datos de entrada y el retorno de informacion de acuerdo a la opción seleccionada
        if (Validarnum(inicprog) == False): 
            #El valor introducido por el usuario no corresponde a un número real
            print("")
            print(Fore.RED+"ERROR:", " El valor introducido no corresponde a un numero entero positivo, por favor intente nuevamente.")
            print("")
            print("")
            
        elif (int(inicprog)> 6) or (int(inicprog)< 1):
            #El número i1
            #introducido por el usuario escapa del rango 1-6
            Errorinic(int(inicprog))
            
        elif (int(inicprog)==6):
            #El usuario seleccionó la funcion 6, por lo tanto se cierra el programa
            print("")
            print(Fore.CYAN+"Gracias por usar nuestro Programa. Hasta Luego!")
            
        elif (int(inicprog)==1):
            #Se llama el procedimiento Textoarr
            Textoarr()
                               
        elif (int(inicprog)==2):           
            #Se llama el procedimiento Printarreglos
            #Los parametros indicados corresponden a los arreglos en texto de los nicknames y claves telefonicas de los clientes
            Printarreglos(nametxt, clavtxt," "," "," "," ") 
            
        elif (int(inicprog)==3):
            #Se inicializa el arreglo de las claves telefonicas codificadas con la misma cantidad de posiciones que el arreglo de las claves telefónicas en texto
            clavcod = np.array(["                        "]*len(clavtxt))
            #Se le asigna a cada posición del arreglo clavcod un valor mediante el uso de un ciclo para
            for i in range(0,len(clavcod),1):
                #Se llama 
                clavcod[i]=Traductor(clavtxt[i])
            #Se inicializa el arreglo de los nicknames codificados con la misma cantidad de posiciones que el arreglo de los nicknames en texto
            namecod=np.array(["                           "]*len(nametxt))
            #Se le asigna a cada posición del arreglo namecod un valor mediante el uso de un ciclo para
            for i in range(0,len(namecod),1):
                namecod[i]=Traductor(nametxt[i])
            print("")
            print(Fore.CYAN+"Se ha codificado de Letras a Codigo Morce.")
            print("")
            print("")
            
        elif (int(inicprog)==4):
            #Se llama el procedimiento Printarreglos
            #Los parametros indicados corresponden a los arreglos codificados y a las palabras auxiliares necesarias para especificarle al usuario que se mostrarán sólo los datos codificados
            Printarreglos(namecod, clavcod," codificados ", " codificadas ", " codificado ", " codificada ")
            
        elif (int(inicprog)==5):
            #El usuario seleccionó la funcion 5, por lo tanto se crea un archivo donde se almacenan tanto el nickname como la clave ya codificados.
            print(Fore.CYAN+"Función 5")
            ArchMorse(clavcod,namecod)
    print("Se ha salido del programa correctamente.")
    #El usuario seleccionó la funcion 6, la cual permite salir del programa.
    
main()