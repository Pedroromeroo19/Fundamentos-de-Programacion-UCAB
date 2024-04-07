def main():
    #Variables Globales
    num1:int
    n1:int
    n2:int
    n3:int
    Pn1:int
    Pn2:int
    Pn3:int
    nf:int
    notama:int()
    
    def Encabezado(nombre:str):
        print("Ucab Elaborado por:", nombre)
        
    def Validar(y:int):
        if(y>99999)and(y<=999999):
            r=True
        else:
            r=False
        return r
    
    def Separar(x:int):
        nonlocal n1,n2,n3
        r1=(x//100)
        n1=(x%100)
        r2=(r1//100)
        n2=(r1%100)
        n3=(r2%100)
        
    def mayornota(x,y,z):
        nonlocal notama
        if(x>y)and(x>z):
            notama=x
        elif(y>x)and(y>z):
            notama=y
        else:
            notama=z

    def porcentaje(a=int, b=int):
        por=((a*b)//100)
        return por
        
    def Sumar(x:int,y:int,z=int):
        suma=(x+y+z)
        return suma
        
        
    #Programa Principal
    #entradas de datos
    Encabezado("Pedro Romero")
    print("Indique un numero entero positivo de 6 digitos, el cual representa sus calificaciones del en una escala del 1-20")
    num1=int(input())
    #procesamiento
    if(Validar(num1)==False):
        print("Error usted a colado un numero incorrecto, su numero es",num1)
        print("Debe ser entero positivo de 6 digitos")
    else:
        Separar(num1)
        mayornota(n1,n2,n3)
        pn1= porcentaje(n1,30)
        pn2= porcentaje(n2,40)
        pn3= porcentaje(n3,30)
        nf=Sumar(pn1,pn2,pn3)
        #Datos de salida
        print("Su primera calificacion es",n1)
        print("Su segunda calificacion es",n2)
        print("Su tercera Calificacion es",n3)
        print("el puntaje de sus notas 1 2 y 3 es:",pn1,pn2,pn3)
        print("Su nota final es", nf)
        print("Su mayor nota es", notama)
    
    
    
main()