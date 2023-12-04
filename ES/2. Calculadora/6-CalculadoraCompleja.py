def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División entre cero"

def main():
    previous_result = None

    while True:
        print("1. Suma")  # Opción para realizar una suma
        print("2. Resta")  # Opción para realizar una resta
        print("3. Multiplicación")  # Opción para realizar una multiplicación
        print("4. División")  # Opción para realizar una división
        print("0. Salir")  # Opción para salir del programa

        choice = input("Ingrese su opción: ")  # Solicitar al usuario que ingrese su opción

        if choice == "0":  # Si la opción es 0, salir del programa
            break

        if choice not in ["1", "2", "3", "4"]:  # Si la opción no es válida, mostrar un mensaje de error y continuar con el ciclo
            print("Opción inválida. Por favor, intente nuevamente.")
            continue

        if previous_result is not None:  # Si hay un resultado anterior disponible
            use_previous_result = input("¿Desea utilizar el resultado anterior? (s/n): ")  # Preguntar al usuario si desea utilizar el resultado anterior
            if use_previous_result.lower() == "s":  # Si el usuario desea utilizar el resultado anterior
                num1 = previous_result  # Asignar el resultado anterior como el primer número
            else:
                num1 = float(input("Ingrese el primer número: "))  # Solicitar al usuario que ingrese el primer número
        else:
            num1 = float(input("Ingrese el primer número: "))  # Solicitar al usuario que ingrese el primer número

        num2 = float(input("Ingrese el segundo número: "))  # Solicitar al usuario que ingrese el segundo número

        if choice == "1":  # Si la opción es 1, realizar una suma
            result = add(num1, num2)
            print("Resultado:", result)
        elif choice == "2":  # Si la opción es 2, realizar una resta
            result = subtract(num1, num2)
            print("Resultado:", result)
        elif choice == "3":  # Si la opción es 3, realizar una multiplicación
            result = multiply(num1, num2)
            print("Resultado:", result)
        elif choice == "4":  # Si la opción es 4, realizar una división
            result = divide(num1, num2)
            print("Resultado:", result)

        previous_result = result  # Guardar el resultado para utilizarlo en la siguiente iteración

        print()

if __name__ == "__main__":
    main()