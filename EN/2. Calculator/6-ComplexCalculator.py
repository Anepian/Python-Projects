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
        return "Error: Division by zero"

def main():
    previous_result = None

    while True:
        print("1. Addition")  # Option to perform addition
        print("2. Subtraction")  # Option to perform subtraction
        print("3. Multiplication")  # Option to perform multiplication
        print("4. Division")  # Option to perform division
        print("0. Exit")  # Option to exit the program

        choice = input("Enter your choice: ")  # Ask the user to enter their choice

        if choice == "0":  # If the choice is 0, exit the program
            break

        if choice not in ["1", "2", "3", "4"]:  # If the choice is not valid, display an error message and continue with the loop
            print("Invalid choice. Please try again.")
            continue

        if previous_result is not None:  # If there is a previous result available
            use_previous_result = input("Do you want to use the previous result? (y/n): ")  # Ask the user if they want to use the previous result
            if use_previous_result.lower() == "y":  # If the user wants to use the previous result
                num1 = previous_result  # Assign the previous result as the first number
            else:
                num1 = float(input("Enter the first number: "))  # Ask the user to enter the first number
        else:
            num1 = float(input("Enter the first number: "))  # Ask the user to enter the first number

        num2 = float(input("Enter the second number: "))  # Ask the user to enter the second number

        if choice == "1":  # If the choice is 1, perform addition
            result = add(num1, num2)
            print("Result:", result)
        elif choice == "2":  # If the choice is 2, perform subtraction
            result = subtract(num1, num2)
            print("Result:", result)
        elif choice == "3":  # If the choice is 3, perform multiplication
            result = multiply(num1, num2)
            print("Result:", result)
        elif choice == "4":  # If the choice is 4, perform division
            result = divide(num1, num2)
            print("Result:", result)

        previous_result = result  # Save the result to use it in the next iteration

        print()

if __name__ == "__main__":
    main()