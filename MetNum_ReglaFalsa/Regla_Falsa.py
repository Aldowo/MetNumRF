import numpy as np
from math import *
from prettytable import PrettyTable
from math import e
import math

#Funcion para insertar la expresion algebraica
def ecuacion():
    expr = input("Ecuacion a evaluar: ")
    return expr

#Funcion para evaluar la expresion algebraica
def funcion(expr, val):
    x = val
    y = eval(expr)
    return y

#Funcion que toma los valores de la interseccion
def valoresI():
    a= float(input("Introduzca el valor de a: "))
    b= float(input("Introduzca el valor de b: "))
    return a,b 

#Funcion para insertar la tolerancia del error
def tolerancia():
    error = float(input("Cantidad de iteraciones a desarrollar:  "))
    error = error+1
    return error

#Entrada de datos
fx=ecuacion() #Pide la ecuacion
Tolerancia=tolerancia() #Pide la tolerancia

#Crea la tabla donde se mostraran las posibles intersecciones
tabla1= PrettyTable(["X","F(X)"])
tabla1.title="Seleccione los valores a considerar"

#Crea la tabla donde se mostraran las raices
tabla2= PrettyTable(["No.","a","f(a)","b","f(b)","c","f(c)","ErrorR","%Error"])
tabla2.title="Metodo de la regla falsa"

#Bucle que evualuca funciones para encontrar las posibles intersecciones
i1=5
while(i1>-6):
    fxP=funcion(fx,i1)
    tabla1.add_row([i1,"{0:.7f}".format(fxP)])
    i1=i1-1

print(tabla1)

#Se piden los valores de a y b deseados
a,b=valoresI()

#Se colocan valores iniciales para iniciar el bucle while
error=1
i=1
cOld=0

#Bucle while en el que se lleva a cabo el metodo
while(i<Tolerancia):
    #Se evalua la funcion para los valores de a y b
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
    tabla2.add_row([i,"{0:.7f}".format(aOld),"{0:.7f}".format(fa),"{0:.7f}".format(bOld),"{0:.7f}".format(fb),
                   "{0:.7f}".format(c),"{0:.7f}".format(fc),"{0:.7f}".format(error),"{0:.7f}".format(error*100)])    
    i=i+1

#Se imprime la tabla al completo
print(tabla2)
c="{0:.5f}".format(c)
#Se imprime la raiz
print(f"La raiz es: {c}")