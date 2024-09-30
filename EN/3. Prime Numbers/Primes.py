def is_prime(number):
    """
    Determines if a number is prime.

    A prime number is one that is only divisible by 1 and itself.

    Args:
        number (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def primes_up_to(n):
    """
    Generates a list of prime numbers up to a given number.

    Args:
        n (int): The upper limit to generate prime numbers.

    Returns:
        list: A list of prime numbers up to the number n.
    """
    primes = []
    for num in range(2, n + 1):
        if is_prime(num):
            primes.append(num)
    return primes