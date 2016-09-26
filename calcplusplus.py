#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import csv
import calcoo
import CalculadoraHija


if __name__ == "__main__":

#lidia
    fichero = sys.argv[1]

    with open('calculadora.csv') as csvarchivo:
        lineas = csv.reader(csvarchivo)
        
        for linea in lineas:
            print(linea)
            resultado = 0
            if linea[0] == "suma":
                linea.pop(0)
                for i in linea:
                    resultado = CalculadoraHija.CalculadoraHija.plus(resultado, int(i))
                print(resultado)
            elif linea[0] == "resta":
                linea.pop(0)
                resultado = int(linea[0])
                for i in linea:
                    resultado = CalculadoraHija.CalculadoraHija.minus(resultado, int(i))
                print(resultado)
            elif linea[0] == "multiplica":
                linea.pop(0)
                resultado = 1
                for i in linea:
                    resultado = CalculadoraHija.CalculadoraHija.multiply(resultado, int(i))
                print(resultado)
            elif linea[0] == "divide":
                linea.pop(0)
                resultado = int(linea[0])*int(linea[0])
                for i in linea:
                    resultado = CalculadoraHija.CalculadoraHija.divide(resultado, int(i))
                print(resultado)

    
    #fichero.close()