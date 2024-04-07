def main():
    # Abrir el Archivo de salida (leer)
    arch=open("d:ventas.txt","rt")    
    print("UCAB Elaborado por:  ")
    sum=0
    for linea in arch.readlines():
        ven=int(linea)
        if(ven>=3500)and(ven<=7500):
            print(linea)
            sum=(sum+ven)        
    arch.close()    
    print()
    print("La Suma de todas las ventas entre 3500 y 7500 es: ",sum)
            
main() 