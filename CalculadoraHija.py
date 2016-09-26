#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoo

class CalculadoraHija(calcoo.Calculadora):
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
    try:
        operando1 = int(sys.argv[1])
        operando2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical parameters")

    if sys.argv[2] == "suma":
        result = CalculadoraHija.plus(operando1, operando2)
    elif sys.argv[2] == "resta":
        result = CalculadoraHija.minus(operando1, operando2)
    elif sys.argv[2] == "dividir":
        result = CalculadoraHija.divide(operando1, operando2)
    elif sys.argv[2] == "multiplicar":
        result = CalculadoraHija.multiply(operando1, operando2)
    else:
        sys.exit('Operación sólo puede ser sumar o restar.')

    print(result)
