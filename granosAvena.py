#!/usr/bin/python3
#coding:utf8

#Si se colocase sobre un tablero de ajedrez (lo suficientemente grande)
#un grano de trigo en el primer casillero, dos en el segundo,
#cuatro en el tercero y así sucesivamente, doblando la cantidad de granos
#en cada casilla, ¿cuántos granos de trigo habría en el tablero?


for i in range(0,64):
    granos = granos + 2**i
#Tambien se podria haber resuelto con el siguiente calculo granos = 2**64 - 1
    
print("La cantidad total de granos en el tablero sera:",granos)
