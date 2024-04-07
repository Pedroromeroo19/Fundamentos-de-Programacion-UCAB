import numpy as np
def main():
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
            retr=""
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
        return retr
    '''Esta funcion cambia una frase completa de letras a codigo morce'''
    def Traductor(frase:str):
        frasemorce=''
        for cont in range(0,len(frase),1):
            Letra=DatostraductorLaCM(frase[cont])
            frasemorce=frasemorce+'  '+Letra
        return frasemorce
    
    #Las siguientes variables dan un ejemplo de como seria un array
    clvtelfarr=np.array(["2371","8215"])
    clvtelfarrmorce=np.array([str("                                ")]*len(clvtelfarr))
    nicknamarr=np.array(["iehl","mehp"])
    nicknamarrmorce=np.array([str("                                ")]*len(nicknamarr))
    
    #
    for cont in range(0,len(clvtelfarr),1):
        clvtelfarrmorce[cont]=Traductor(clvtelfarr[cont])
        
    for cont in range(0,len(nicknamarr),1):
        nicknamarrmorce[cont]=Traductor(nicknamarr[cont])
    
    print("Entradas en clave telefono array:",*clvtelfarr)
    print("Salida clave telefono array en codigo morce",clvtelfarrmorce)
    print("Entradas en nick name array:",*nicknamarr)
    print("Salida nick name array en codigo morce",nicknamarrmorce)
    
    '''print('Ingrese una frase sin espacios')
    fras=input()
    x=traductor(fras)
    print(x)'''
main()