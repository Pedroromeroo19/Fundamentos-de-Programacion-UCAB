def main():
    # Abrir el Archivo de salida (leer)
    arch=open("d:ventas.txt","rt")
    print("UCAB Elaborado por:  ")
    print("Los datos del archivo ventas son: ")
    #print(arch.read())
    for linea in arch.readlines():
        print(linea)        
    arch.close()        
main() 