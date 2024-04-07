def main():
    #Variables globales
    n:int
    n1:int
    n2:int
    sum:int
    
    def Encabezado(nombre:str):
        print("Ucab Elaborado por:", nombre)
        
    def Validar(y:int):
        if(y>999)and(y<=9999):
            r=True
        else:
            r=False
        return r
        
    def Separar(y:int):
        nonlocal n1,n2
        n1=(y//100)
        n2=(y%100)
        
        #return n1,n2
        
    def Sumar(x:int,y:int):
        suma=(x+y)
        return suma
        
    #Programa principal
    #Entrada de datos
    Encabezado("Pedro Romero")
    print("Indique un numero entero positivo de 4 digitos")
    n=int(input())
    #Procesamiento
    if(Validar(n)==False):
        print("Error usted a colado un numero incorrecto, su numero es",n)
        print("Debe ser entero positivo de 4 digitos")
    else:
        Separar(n)
        sum=Sumar(n1,n2)
        #Salida de datos
        print("Su numero es", n)
        print("Los primeros 2 digitos del numero son", n1)
        print("Los ultimos 2 digitos del numero son", n2)
        print("La suma de los 2 numeros anteriores son", sum)
    
    #taller n3 funcion separar
    #def Separar(y):
        #if(c1==y)
            #c1n1=(y//1000)
            #c1n2=(y%1000)
        #elif(c2==y):
            #c2n1=(y//1000)
            #c2n2=(y%1000)
        #else:
            #c3n1=(y//1000)
            #c3n2=(y%1000)
main()