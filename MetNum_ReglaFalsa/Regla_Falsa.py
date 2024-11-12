import numpy as np
from math import *
from prettytable import PrettyTable
#Funcion para insertar la expresion algebraica
def ecuacion():
    expr = input("Ecuacion a evaluar: ")
    return expr

#Funcion para evaluar la expresion algebraica
def funcion(expr, val):
    x = val
    y = eval(expr)
    return y

#Funcion para insertar la tolerancia del error
def tolerancia():
    error = float(input("Tolerancia del error:  "))
    return error

fx=ecuacion() #Pide la ecuacion
Tolerancia=tolerancia() #Pide la tolerancia

faP=5   #Establece un valor para iniciar el bucle while
i1=10000 #Establece desde que valor se evaluara hasta conseguir el cambio de signo
#Bucle que evalua i1
while(faP>0):
    faP=funcion(fx,i1)
    i1=i1-1
#Se colocan los valores y se corrigen
a=i1+1
b=i1+2
#Crea una tabla
tabla= PrettyTable(["No.","a","f(a)","b","f(b)","c","f(c)","ErrorR","%Error"])
tabla.title="Metodo de la regla falsa"
#Se colocan valores iniciales para iniciar el bucle while
error=abs(b-a)
i=1
cOld=0
#Bucle while en el que se lleva a cabo el metodo
while(error>Tolerancia):
    #Se evaluan la funcion para los valores de a y b
    fa= funcion(fx,a)
    fb= funcion(fx,b)
    #Se calcula c y se evalua
    c= (a*fb-b*fa)/(fb-fa)
    fc=funcion(fx,c)

    aOld=a
    bOld=b

    #Se calcula el error relativo
    error=abs((c-cOld)/(c))
    cOld=c
    #Se hace el cambio de posicion segun el signo de la funcion c
    if fc<0:
        a=c
    else:
        b=c
    #Se agrega una fila donde se insertaran los valores de esta iteracion    
    tabla.add_row([i,"{0:.7f}".format(aOld),"{0:.7f}".format(fa),"{0:.7f}".format(bOld),"{0:.7f}".format(fb),
                   "{0:.7f}".format(c),"{0:.7f}".format(fc),"{0:.7f}".format(error),"{0:.7f}".format(error*100)])    
    i=i+1
#Se imprime la tabla al completo
print(tabla)
c="{0:.5f}".format(c)
#Se imprime la raiz
print(f"La raiz es: {c}")