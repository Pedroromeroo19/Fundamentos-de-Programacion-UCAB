def main():
    print("Ucab Elaborado por: Pedro Romero")
    print("Los datos del archivo son")
    arch=open("C:\\Users\\Pedro\\OneDrive\\Desktop\\Estudios Ucab\\Semestre 1\\Fundamentos de Programacion\\Semana 12 FP\\Nombres.txt","rt")
    #print(arch.read())
    
    # Para leer linea por linea
    
    for linea in arch.readlines():
        #hacer algo con cada linea de archivo
        print(linea)
        #num=int(linea)
        
    #arch.close()
main()