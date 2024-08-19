# calculadora.py 

import math 

def sumar(a, b):
    return a + b

def Resta(a, b):
    return a - b

def Mult(a, b):
    return a * b
    
def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero no permitida."
