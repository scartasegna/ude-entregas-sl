#!/usr/bin/python3
#coding:utf8

def calculoSalario(bruto):
    """Funcion que dado un sueldo el bruto, calcula el Salario liquido"""
    descuentos = calcularDescuentos(bruto)
    return(bruto - descuentos)

def calcularDescuentos(bruto):
    """Esta funcion calcula los descuentos segun el apunte retorna el descuento
    total y los imprime por separado"""
    descuentos = 0
    #IR es el 11%
    ir = bruto * 0.11
    #INSS es 8%
    inss = bruto * 0.08
    #sindicato es 5%
    sindicato = bruto * 0.05
    print("Descuentos aplicados")
    print("-------------")
    print("IR:",-ir)
    print("INSS:",-inss)
    print("Sindicato:",-sindicato)
    print("-------------")
    return (ir+inss+sindicato)

precio=float(input("Ingrese el monto por hora que ud gana:"))
hora=float(input("Ingrese la cantidad de horas trabajadas:"))
bruto = precio * hora
print("El salario bruto es:",bruto)
liquido = calculoSalario(bruto)
print("El salario liquido resultante es",liquido)
