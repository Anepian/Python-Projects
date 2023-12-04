# Simple Calculator

# Function to add two numbers
def add(a, b):
    """
    This function takes two numbers and returns their sum.
    """
    return a + b

# Function to subtract two numbers
def subtract(a, b):
    """
    This function takes two numbers and returns their difference.
    """
    return a - b

# Function to multiply two numbers
def multiply(a, b):
    """
    This function takes two numbers and returns their product.
    """
    return a * b

# Function to divide two numbers
def divide(a, b):
    """
    This function takes two numbers and returns their quotient.
    """
    if b != 0:
        return a / b
    else:
        return "Error: Cannot divide by zero."

# Main function
def main():
    print("Simple Calculator")
    print("-----------------")
    print("Available operations:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("-----------------")

    operation = input("Enter the name of the operation: ")

    if operation in ["Add", "Subtract", "Multiply", "Divide"]:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if operation == "Add":
            result = add(num1, num2)
            print("The result of the addition is:", result)
        elif operation == "Subtract":
            result = subtract(num1, num2)
            print("The result of the subtraction is:", result)
        elif operation == "Multiply":
            result = multiply(num1, num2)
            print("The result of the multiplication is:", result)
        elif operation == "Divide":
            result = divide(num1, num2)
            print("The result of the division is:", result)
    else:
        print("Invalid operation. Please enter a valid operation.")

# Call the main function
if __name__ == "__main__":
    main()