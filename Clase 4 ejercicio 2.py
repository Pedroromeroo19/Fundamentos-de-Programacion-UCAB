def main():
    print("UCAB Elaborado por: Pedro Romero ")
    print()
    
    #Datos de entrada
    print("Vamos a sumar el numero indicado por usted, cierta cantidad de veces con el metodo que usted desee")
    print("Indique un numero entero que va a sumar")
    n1=int(input())
    print("Indique un numero entero que representa la cantidad de veces que va a sumar el numero")
    n2=int(input())
    print("indique 1 para while o 2 para for, no indique numero mayor a 2.")
    condicional=int(input())
    
    cont=0
    sum=0
    
    #Procesamiento
    if(condicional==int(1)):
        while(cont<n2):
            sum += n1
            cont += 1
    else:
        for cont in range (n2):
            sum += n1
        
    
    #Datos de salida
    print("El resultado de la suma de", n1, ", la siguiente cantidad de veces:", n2, "es igual a", sum)
main()