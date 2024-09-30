def es_primo(numero):
    """
    Determina si un número es primo.

    Un número primo es aquel que solo es divisible por 1 y por sí mismo.

    Args:
        numero (int): El número a verificar.

    Returns:
        bool: True si el número es primo, False en caso contrario.
    """
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def primos_hasta(n):
    """
    Genera una lista de números primos hasta un número dado.

    Args:
        n (int): El límite superior para generar números primos.

    Returns:
        list: Una lista de números primos hasta el número n.
    """
    primos = []
    for num in range(2, n + 1):
        if es_primo(num):
            primos.append(num)
    return primos

def principal():
    """
    Función principal para verificar si un número proporcionado por el usuario es primo.
    """
    try:
        numero = int(input("Ingrese un número para verificar si es primo: "))
        if es_primo(numero):
            print(f"{numero} es un número primo.")
        else:
            print(f"{numero} no es un número primo.")
    except ValueError:
        print("Por favor, ingrese un número entero válido.")

if __name__ == "__main__":
    principal()