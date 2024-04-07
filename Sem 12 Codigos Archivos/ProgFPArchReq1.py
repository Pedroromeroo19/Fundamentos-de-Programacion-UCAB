def main():
    # Abrir el Archivo de entrada (escribir)
    arch=open("d:ventas.txt","wt")
    r="S"
    print("UCAB Elaborado por:  ")
    while(r=="S"):
        print("Desea ingresar información al Archivo ventas ( S/N )")
        r=input()
        if(r=="S"):
            print("Indique número entero positivo correspondiente a la venta: ")
            n=input()
            arch.write(n)    
            arch.write("\n")
    arch.close()
    print(" Archivo creado y datos almacenados")
        
main() 