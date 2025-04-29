print("A very simple calculator")


while True:
    try:
        operator = input(
            "Enter the operator (+, -, *, /, add, subtract, multiply, divide): ")
        if operator not in ('+', '-', '*', '/', 'add', 'subtract', 'multiply', 'divide'):
            print("Invalid operator. Please try again.")
            continue
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if operator == '+' or operator == 'add':
            print(f"The result of addition {num1} + {num2} is: {num1 + num2}")
        elif operator == '-' or operator == 'subtract':
            print(
                f"The result of subtraction {num1} - {num2} is: {num1 - num2}")
        elif operator == '*' or operator == 'multiply':
            print(
                f"The result of multiplication {num1} * {num2} is: {num1 * num2}")
        elif operator == '/' or operator == 'divide':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                print(
                    f"The result of division {num1} / {num2} is: {num1 / num2}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")
    except KeyboardInterrupt:
        print("\nExiting the calculator. Goodbye!")
        break
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    restart = input(
        "Do you want to perform another calculation? (yes/no): ").lower()
    if restart.startswith('n'):
        print("Goodbye!")
        break
    elif restart != 'yes':
        print("Invalid input. Exiting the calculator.")
        break
