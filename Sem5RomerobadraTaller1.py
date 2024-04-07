def main():
    #entradas de datos
    print("UCAB Elaborado por: Pedro Romero y Georges Badra")
    print("Vamos a Mezclar la pintura que desees, Asegurate que los colores sean diferentes")
    print("indique el primer color de pintura que usted desea mezclar, que puede ser amarillo (10), azul(15)  o rojo (20), segun el precio")
    color1=int(input())
    print("Indique el segundo colo10r de pintura que usted desea mezclar, que puede ser amarillo (10) , azul (15) o rojo (20) segun el precio")
    color2=int(input())
    
    #variables
    
    colorresultante=int(color1+color2)
    
    preciopote=int()
    
    coloresmezclados=str()
    
    costodepote=(color1+color2)
    
    ganancias2pote=int()
    
    #Procesamiento
    
    if ((colorresultante)==25):
        print("su color es verde")
        coloresmezclados=("sus colores mezclados son amarillo (10) y azul (15)")
        preciopote=30
        ganancias2pote=(preciopote-costodepote)
    elif ((colorresultante)==35):
        print("su color es violeta")
        coloresmezclados=("sus colores mezclados son rojo (20) y azul (15)")
        preciopote=35
        ganancias2pote=(preciopote-costodepote)
    elif ((colorresultante)==30):
        print("su color es naranja")
        coloresmezclados=("sus colores mezclados son amarillo (10) y rojo (20)")
        preciopote=40
        ganancias2pote=(preciopote-costodepote)
    else:
        print("usted a colocado el numero equivocado")
    
        
    gananciaspote=(ganancias2pote//2)
    
    Porcentajedeg=(((preciopote-costodepote)/costodepote)*100)
    
    
    #Salida de datos
    if (colorresultante==25)or(colorresultante==35)or(colorresultante==30):
        print(coloresmezclados)
        print("el costo del pote es", costodepote )
        print("su ganancia al mezclar los colores por pote de color primario es", gananciaspote)
        print("su ganancia por pote de color secundario es", ganancias2pote)
        print("su porcentaje de ganancia es", Porcentajedeg, "porciento")
    else:
        print("intentelo otra vez")
main()