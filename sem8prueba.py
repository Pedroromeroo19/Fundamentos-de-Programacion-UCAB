import colorama
from colorama import *
init(autoreset=True)
def main():
    nom=(Fore.BLUE+"Pedro Romero")
    print(Fore.MAGENTA+"UCAB Elaborado por: ",nom)
    
    c1="papa es grande"
    
    print("la cadena original es")
    print(c1)
    
    for i in range(1,len(c1)-1,1):
        if(c1[i]!=" ")and(c1[i]!="."):
            
        else:
            c4=" "
            
main()