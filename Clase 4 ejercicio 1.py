def main():
    print("UCAB Elaborado por: Pedro Romero ")
    print()
    print("indique numero mayor que 30")
    n=int((input()))
    cont=0
    x=n
    sum=0
    while(cont<5):
        print(x)
        cont +=1
        sum=(sum+x) #sum +=x
        x -=1
    print("la suma es", sum)

main()