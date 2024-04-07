import random
import numpy as np
def main():
    notas=np.array([int(0)]*15)
    print("las calificaciones son")
    
    for i in range(0,15,1):
        notas[i]=random.randint(0,20)
       
    print(*notas) 
    print("")
    
    aprobadossum=0
    cantaprob=0
    promaprob=0
    
    reprobadossum=0
    cantreprob=0
    promreprob=0
    
    for i in range(0,15,1):
        if((notas[i])>=10):
            aprobadossum=aprobadossum+notas[i]
            cantaprob=cantaprob+1
            promaprob=(aprobadossum//cantaprob)
        if((notas[i])<10):
            reprobadossum=reprobadossum+notas[i]
            cantreprob=cantreprob+1
            promreprob=(reprobadossum//cantreprob)
    print("el promedio de los aprobados es",promaprob)
    print("el promedio de los reprobados es",promreprob)
    print("la suma de aprobados es", aprobadossum )
    print("la suma de reprobados es", reprobadossum)
main()