import numpy as np
def main():
    p=np.array([4,4,0,0,0])
    arch = open("d:puntos1.txt","wt")
        
    for i in range(0,5,1):
        x=str(p[i])
        arch.write(x)
        arch.write("\n")  
        
    arch.close()
    
    arch = open("d:puntos1.txt","rt")
    print("UCAB Elaborado por:   ")
    print("Los puntos del Estudiante son: ")
    
    for linea in arch.readlines():
        print(linea)
        
    arch.close()    
main()