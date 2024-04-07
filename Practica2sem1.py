import numpy as np
from colorama import *
init(autoreset=True)
def main():
    #datos de entrada
    print("Porfavor ingrese su cedula de identidad")
    cedula=input()
    print("Porfavor ingrese el monto de su compra en dolares")
    monto=int(input())
    print("porfavor indique el precio del dolar de hoy en bolivares")
    dolar=int(input())
    #procesamiento
    totalapagar=(dolar*monto)
    iva=((totalapagar/100)*16)
    totalmasiva=(totalapagar+iva)
    #datos de salida
    print("su cedula es", cedula)
    print("su monto a pagar en dolares es", monto)
    print("su monto a pagar en bolivares es", totalapagar)
    print("el precio del dolar es", dolar)
    print("su monto a pagar mas iva es", totalmasiva)
main()