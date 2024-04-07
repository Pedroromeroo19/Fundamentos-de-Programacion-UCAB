import colorama
from colorama import *
init(autoreset=True)
import random
import numpy as np
def main():
    n=np.array([3,1,8,7,4])
    print("los valores del arreglo son :")
    print(*n)
    print()
    sum=0
    for i in range(0,5,1):
        sum=(sum+n[i])
    print(sum)
main()