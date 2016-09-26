#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import csv
import calcoo
import CalculadoraHija


if __name__ == "__main__":


    fichero = sys.argv[1]
    fichero = open(fichero,'r')
  
    for line in fichero:
        operandos = []
        resultado = 0
        for word in line.split(","):
            operandos.append(word)
        print(operandos)
        if operandos[0] == "suma":
            operandos.pop(0)
            for i in operandos:
                resultado = CalculadoraHija.CalculadoraHija.plus(resultado, int(i))
            print(resultado)
        elif operandos[0] == "resta":
            operandos.pop(0)
            resultado = int(operandos[0])
            for i in operandos:
                resultado = CalculadoraHija.CalculadoraHija.minus(resultado, int(i))
            print(resultado)
        elif operandos[0] == "multiplica":
            operandos.pop(0)
            resultado = 1
            for i in operandos:
                resultado = CalculadoraHija.CalculadoraHija.multiply(resultado, int(i))
            print(resultado)
        elif operandos[0] == "divide":
            operandos.pop(0)
            resultado = int(operandos[0])*int(operandos[0])
            for i in operandos:
                resultado = CalculadoraHija.CalculadoraHija.divide(resultado, int(i))
            print(resultado)

    
    fichero.close()