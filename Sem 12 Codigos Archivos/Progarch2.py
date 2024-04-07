import numpy as np
def main():
    p=np.array([0]*5)
    arch = open("e:puntos.txt","rt")
    #print(f.read())
    i=0 
    for linea in arch.readlines():
        # Hacer algo con cada línea del archivo.
        #print(line)
        p[i]=linea
        i +=1
    arch.close()
    print("UCAB Elaborado por:   ")
    print("Los puntos del Estudiante son: ")
    sum=0
    for i in range(0,5,1):
        print(p[i],end=" ")
        sum=(sum+p[i])
    print()
    print("La Nota del Estudiante es: ",sum)

    
main()