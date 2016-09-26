#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

class Calculadora():
    def plus(op1, op2):
        """ Function to sum the operands """
        return op1 + op2


    def minus(op1, op2):
        """ Function to substract the operands """
        return op1 - op2

class CalculadoraHija(Calculadora):
    def multiply(op1, op2):
        """ Function to sum the operands """
        return op1 * op2


    def divide(op1, op2):
        """ Function to substract the operands """
        try:
            resultado = op1 / op2
        except ZeroDivisionError:
            sys.exit("Error: division by zero")
        return resultado


if __name__ == "__main__":


    fichero = sys.argv[1]
    fichero = open(fichero,'r')
  
    for line in fichero:
        operandos = []
        resultado = 0
        for word in line.split(","):
            operandos.append(word)
        print(operandos)
        if operandos[0] == "sumar":
            operandos.pop(0)
            for i in operandos:
                resultado = resultado + int(i)
            print(resultado)
        elif operandos[0] == "restar":
            operandos.pop(0)
            for i in operandos:
                resultado = resultado - int(i)
            print(resultado)


    
    fichero.close()