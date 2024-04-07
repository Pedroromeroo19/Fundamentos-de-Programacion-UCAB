import colorama
from colorama import *
init(autoreset=True)
def main():
    c1=Fore.RED+".hermosa y linda es casa La"
    nom=(Fore.BLUE+"Rodolfo Holguin")
    print(Fore.MAGENTA+"UCAB Elaborado por: ",nom)
    
    """x=len(c1)-1
    print(x)
    print(c1[x])
    for i in range (len(c1)-1,0,-1):
        print(c1[i],end=" ")"""

    print(Fore.BLUE+"La Cadena Original es: ")
    print(c1) 
    c2=" "       
    c5=" "    
    for i in range(len(c1)-1,-2,-1):
        if(c1[i]!=" ")and(c1[i]!="."):
            c2=c2+c1[i]
        else:
            c4=" "
            for j in range(len(c2)-1,-1,-1):
                c4=(c4+c2[j])            
            c5=(c5+c4)
            c4=" "
            c2=" "
    c5=(Fore.RED+c5+".")
    print(Fore.BLUE+"La cadena Original Invertida es: ")        
    print(c5)

main()