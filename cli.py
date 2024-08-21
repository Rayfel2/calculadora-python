# cli.py
from calculadora import sumar

def main():
    while True:
        print("Opciones:")
        print("1. Sumar")
        print("2. Salir")
        
        eleccion = input("Elige una opción: ")
        
        if eleccion == '2':
            break
        
        if eleccion == '1':
            num1 = float(input("Introduce el primer número: "))
            num2 = float(input("Introduce el segundo número: "))
            print(f"Resultado: {sumar(num1, num2)}")
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()
