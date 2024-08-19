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

def factorial(n):
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos")
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursivo(n - 1)
