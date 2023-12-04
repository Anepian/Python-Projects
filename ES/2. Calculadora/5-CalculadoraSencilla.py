# Calculadora sencilla

# Función para sumar dos números
def sumar(a, b):
    """
    Esta función recibe dos números y devuelve la suma de ellos.
    """
    return a + b

# Función para restar dos números
def restar(a, b):
    """
    Esta función recibe dos números y devuelve la resta de ellos.
    """
    return a - b

# Función para multiplicar dos números
def multiplicar(a, b):
    """
    Esta función recibe dos números y devuelve el producto de ellos.
    """
    return a * b

# Función para dividir dos números
def dividir(a, b):
    """
    Esta función recibe dos números y devuelve el cociente de la división entre ellos.
    """
    if b != 0:
        return a / b
    else:
        return "Error: No se puede dividir entre cero."

# Función principal
def main():
    print("Calculadora sencilla")
    print("--------------------")
    print("Operaciones disponibles:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("--------------------")

    operacion = input("Ingrese el nombre de la operación: ")

    if operacion in ["Sumar", "Restar", "Multiplicar", "Dividir"]:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))

        if operacion == "Sumar":
            resultado = sumar(num1, num2)
            print("El resultado de la suma es:", resultado)
        elif operacion == "Restar":
            resultado = restar(num1, num2)
            print("El resultado de la resta es:", resultado)
        elif operacion == "Multiplicar":
            resultado = multiplicar(num1, num2)
            print("El resultado de la multiplicación es:", resultado)
        elif operacion == "Dividir":
            resultado = dividir(num1, num2)
            print("El resultado de la división es:", resultado)
    else:
        print("Operación inválida. Por favor, ingrese una operación válida.")

# Llamada a la función principal
if __name__ == "__main__":
    main()