def main():
    #Dada una cadena que inicia por punto y esta escrita
    #al reves, se desea generar a partir de esta que este 
    #al derecho y termine en punto.
     
    c1=".bella linda playa"    
    c2=""
    c4=""
    
    print("UCAB Elaborado por:      ") # Colocar su Nombre
    print("La Cadena Original es: ")
    print(c1)  
    #Primero se extrae palabra por palabra de la cadena c1
    #del final al principio porque la ultima palabra de c1
    #debe de estar de primera, recordandose que la palabra
    #extraida quedara al reves y que se incluye en la 
    #condicion de parada el punto que esta al principio
    #para que sea tomada en cuenta la primera Letra de c1
    # Los Parametros del Range son:
    #len(c1)-1 = ultima posicion valida de c1    
    #-1 = Porque el segundo parametro se detiene 
    #     en uno menos que es 0 primera posicion valida de c1
    #-1 = Para recorerla en forma regresiva (final al principio) 
    for i in range(len(c1)-1,-1,-1):
        if(c1[i]!=" ")and(c1[i]!="."):
            c2=(c2+c1[i])
        else:
            print(c2)  #Para que se vea que cada palabra esta
                       #invertida (no es necesario mostrar) 
            c3=""
            # Para Invertir la palabra de c2
            for j in range(len(c2)-1,-1,-1):
                c3=c3+c2[j]
            print(c3) #Para que se vea que se volteo
                      #la palabra invertida (no es necesario mostrar) 
            # Se CONCATENA la palabra derecha en la cadena final
            # palabra por palabra y el espacio
            # en blanco
            c4=c4+c3+" "
            c2="" #se inicializa c2 para ser
                  #utilizada nuevamente  
    c4=c4+"."  # Se concatena con el punto
    print("La Cadena Final es: ")
    print(c4)          
            
main() 