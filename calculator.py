# Simple Calculator in Python by institute

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

def calculator():
    print("Simple Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    try:
        choice = int(input("Enter choice (1/2/3/4): "))
        if choice not in [1, 2, 3, 4]:
            print("Invalid choice! Please choose a valid option.")
            return

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == 1:
            print(f"The result is: {add(num1, num2)}")
        elif choice == 2:
            print(f"The result is: {subtract(num1, num2)}")
        elif choice == 3:
            print(f"The result is: {multiply(num1, num2)}")
        elif choice == 4:
            print(f"The result is: {divide(num1, num2)}")

    except ValueError:
        print("Invalid input! Please enter numeric values.")

# Run the calculator
calculator()
