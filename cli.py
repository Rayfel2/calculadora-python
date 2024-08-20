# cli.py reload
from calculadora import sumar, resta, mult, dividir, potencia

def main():
    while True:
        print("Opciones:")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Potencia")
        print("6. Salir")
        
        eleccion = input("Elige una opción: ")
        
        if eleccion == '5':
            break
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))
        
        if eleccion == '1':
            print(f"Resultado: {sumar(num1, num2)}")
        elif eleccion == '2':
            print(f"Resultado: {resta(num1, num2)}")
        elif eleccion == '3':
            print(f"Resultado: {mult(num1, num2)}")
        elif eleccion == '4':
            print(f"Resultado: {dividir(num1, num2)}")
        elif eleccion == '5':
            print(f"Resultado: {potencia(num1, num2)}")
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()


