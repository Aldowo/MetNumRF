import numpy as np
from math import *
from prettytable import PrettyTable
from math import e
import math

def ecuacion():
    expr = input("Ecuacion a evaluar: ")
    return expr

def funcion(expr, val):
    x = val
    y = eval(expr)
    return y

def valoresI():
    a= float(input("Introduzca el valor de a: "))
    b= float(input("Introduzca el valor de b: "))
    return a,b 

def tolerancia():
    error = float(input("Cantidad de iteraciones a desarrollar:  "))
    error = error+1
    return error

def tablaRaiz(fx):
    i1=15
    tabla1= PrettyTable(["X","F(X)"])
    tabla1.title="Seleccione los valores a considerar"
    while(i1>-16):
        fxP=funcion(fx,i1)
        tabla1.add_row([i1,"{0:.7f}".format(fxP)])
        i1=i1-1
    print(tabla1)

def Metodo(a,b,fx,cs):
    
    tabla2= PrettyTable(["No.","a","f(a)","b","f(b)","c","f(c)","ErrorR","%Error"])
    tabla2.title="Metodo de la regla falsa"
    
    error=1
    i=1
    cOld=0

    
    while(i<Tolerancia):
        fa= funcion(fx,a)
        fb= funcion(fx,b)
        c= (a*fb-b*fa)/(fb-fa)
        fc=funcion(fx,c)

        aOld=a
        bOld=b

        error=abs((c-cOld)/(c))
        cOld=c
        
        if fc<0:
            a=c
        else:
            b=c
    
        tabla2.add_row([i,round(aOld,cs),round(fa,cs),round(bOld,cs),round(fb,cs),
                    round(c,cs),round(fc,cs),round(error,cs),round(error*100,cs)])    
        i=i+1

    print(tabla2)
    Credondo=round(c,cs)
    print(f"La raiz es: {Credondo}")
    


#Entrada de datos

opc=5
opc2=5
while opc!=0:

    print("Menu principal")
    print("1)Calcular raiz")
    print("0)Salir del programa")
    
    opc=float(input())
    
    if opc==1:
        x=ecuacion() 
        opc2=5
        while opc2!=0 and opc2!=2:
            tablaRaiz(x)
            a,b=valoresI()
            print("Cuantas cifras quiere redondear?: ")
            fix= int(input())
            Tolerancia=tolerancia() 
            Metodo(a,b,x,fix)
    
            print("Seleccione la operacion a realizar: ")
            print("1)Calcular otra raiz con la misma funcion")
            print("0)Regresar al menu principal")
            
            opc2=float(input())
    else:
        print("Saliendo...")

