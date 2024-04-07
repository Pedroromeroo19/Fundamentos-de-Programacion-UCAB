import colorama
from colorama import *
init(autoreset=True)
import random
import numpy as np
def main():
    n=np.array([""]*5)
    print("los valores del arreglo son :")
    for i in range(0,5,1):
        x=random.randint(97,122)
        n[i]=chr(x)
    
    print(*n)
    conta=0
    for l in range(0,5,1):
        if(n[l]=="a"):
            conta=(conta+1)

    print("la cantidad de a es", conta)
main()
