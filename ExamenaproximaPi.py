#!/usr/bin/python
#coding:utf8

# Hacer un programa que haga una aproximacion a Pi con N terminos
# usando la siguiente formula
# pi = 4/1 - 4/3 + 4/7 - 4/9 ...

def aproximaPi(numeroAprox):
    pi=4
    for i in range(2,numeroAprox+1):
        if ( i % 2==0):
            #Si es termino par es la resta del siguiente numero impar
            pi = pi - (4/(i+1))
        else:
            #Sino, es la suma
            pi = pi + (4/i)
    return pi


cantidad =int(input("Ingrese el numero de veces que quiere que se aproxime: "))

pi =  aproximaPi(cantidad)

print("La aproximacion de pi es:", pi)
        
