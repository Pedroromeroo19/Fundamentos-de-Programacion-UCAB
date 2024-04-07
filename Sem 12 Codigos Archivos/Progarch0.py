def main():
    print("UCAB Elaborado por:  ")
    print("Los datos del Archivo son: ")    
    arch = open("g:nombres.txt","rt")
    #print(arch.read()) 
    
    # Para leer linea por linea
            
    for linea in arch.readlines():
        # Hacer algo con cada línea del archivo.        
        print(linea)
    arch.close()
main()