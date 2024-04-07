def main():
    #Var Globales
    inter:int
    
    def Encabezado(nombre:str):
        print("Ucab Elaborado por:", nombre)
    #Funciones de validacion
    def Validarc1(y:int):
        if(y>99999)and(y<=999999):
            r=True
        else:
            r=False
        return r
    
    def Validarc2(z:int):
        if(z>99999)and(z<=999999):
            r=True
        else:
            r=False
        return r
    
    def Validarc3(u:int):
        if(u>99999)and(u<=999999):
            r=True
        else:
            r=False
        return r
    
    #funciones de separacion
    def Separarpri3dig(y):
        r=(y//1000)
        return r
    def separarult3dig(u):
        r=(u%1000)
        return r
    
    def caycu(ca:int,cu:int):
        nonlocal inter
        if ca>cu:
            ce=ca-cu
            inter=((ca*20)//100)+((ce*40)//100)
        else:
            inter=((ca*20)//100)
            return inter
            
    def crerest(x:int,y:int):
        if x>y:
            cr=x-y
        else:
            cr=x-y
        return cr
    #Procedimientos y funciones
    
    #Programa Principal
    Encabezado("Pedro Romero y Samuel Sangroni")
    print("Coloque un numero entero positivo de 6 digitos")
    c1=int(input())
    print("Coloque un numero entero positivo de 6 digitos")
    c2=int(input())
    print("Coloque un numero entero positivo de 6 digitos")
    c3=int(input())
    
    if((Validarc1(c1)and(Validarc2(c2))and(Validarc3(c3)))==False):
        print("Error usted a puesto numeros que son incorrectos, sus numero son",c1,c2,c3)
        print("Debe ser entero positivo de 6 digitos")
    else:
        c1cu=Separarpri3dig(c1)
        c1ca=separarult3dig(c1)
        c2cu=Separarpri3dig(c2)
        c2ca=separarult3dig(c2)
        c3cu=Separarpri3dig(c3)
        c3ca=separarult3dig(c3)
        inter1=caycu(c1ca,c1cu)
        inter2=caycu(c2ca,c2cu)
        inter3=caycu(c3ca,c3cu)
        crc1=crerest(c1ca,c1cu)
        crc2=crerest(c2ca,c2cu)
        crc3=crerest(c3ca,c3cu)
        print("Los numeros indicados son",c1,c2,c3)
        print("El credito aprobado de el cliente uno es", c1ca, "Y el credito utilizado fue", c1cu)
        print("El credito aprobado de el cliente dos es", c2ca, "Y el credito utilizado fue", c2cu)
        print("El credito aprobado de el cliente tres es", c3ca, "Y el credito utilizado fue", c3cu)
        print("el credito restante del primer cliente es", crc1)
        print("el credito restante del segundo cliente es", crc2)
        print("el credito restante del tercer cliente es", crc3)
        print("El interes del cliente uno es",inter1)
        print("El interes del cliente dos es",inter2)
        print("El interes del cliente tres es",inter3)
main()