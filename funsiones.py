def suma(a, b):
    return(a + b)
def resta(a, b):
    return(a - b)
def multiplicacion(a, b):
    return(a * b)
def division(a, b):
    if a == 0:
        return("No se puede dividir por 0.")
    else:
        return(a / b)
op = 0
while op != 5:
    op = int(input("\nBienvenido a la calculadora\n Ingrese la acción que desea realizar\n1. Suma\n2. Resta\n3. Multiplicación\n4. División\n5. Salir\n"))
    if op == 1:
        num1 = int(input("Ingrese el primer número a sumar: "))
        num2 = int(input("Ingrese el segundo número a sumar: "))
        print(f"El resultado de la suma es {suma(num1,num2)}.")
    elif op == 2:
        num1 = int(input("Ingrese el primer número a restar: "))
        num2 = int(input("Ingrese el segundo número a restar: "))
        print(f"El resultado de la resta es {resta(num1,num2)}.")
    elif op == 3:
        num1 = int(input("Ingrese el primer número a multiplicar: "))
        num2 = int(input("Ingrese el segundo número a multiplicar: "))
        print(f"El resultado de la multiplicación es {multiplicacion(num1,num2)}.")
    elif op == 4:
        num1 = int(input("Ingrese el primer número a dividir: "))
        num2 = int(input("Ingrese el segundo número a dividir: "))
        print(f"El resultado de la división es {division(num1,num2)}.")
    elif op == 5:
        print("Saliendo de la calculadora...")
    else:
        print("Opción inválida.")