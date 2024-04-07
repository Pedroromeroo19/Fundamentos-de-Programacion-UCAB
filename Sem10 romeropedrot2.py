import numpy as np
def main():
    
    print("UCAB Elaborado por: Pedro Luis Romero Bello")
    
    #Datos de entrada
    print("Porfavor indique una frase con letras MINUSCULAS y solamente terminada en punto")
    C1=input()
    
    c2=str()
    for j in range(0,len(C1)-1,1):
        if (C1[j]!="a")and(C1[j]!="e")and(C1[j]!="i")and(C1[j]!="o")and(C1[j]!="u"):
                c2=(c2+C1[j])
    c2=c2+"."
    
    #Datos de salida
    print(" ")
    print("Su cadena es:")
    print(C1)
    print("")
    print("Su cadena sin vocales es:")
    print(c2)
main()