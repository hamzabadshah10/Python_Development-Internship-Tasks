print("Welcome to the Simple Python Calculator")

try:
    first_number = float(input("Enter the first number: "))
    operator = input("Enter an operator (+, -, *, /, %, //, **): ")
    second_number = float(input("Enter the second number: "))

    if operator == '+':
        result = first_number + second_number

    elif operator == '-':
        result = first_number - second_number

    elif operator == '*':
        result = first_number * second_number

    elif operator == '/':
        if second_number != 0:
            result = first_number / second_number

        else:
            result = "Error: Cannot divide by zero."

    elif operator == '%':
        if second_number != 0:
            result = first_number % second_number

        else:
            result = "Error: Cannot perform modulus by zero."

    elif operator == '//':
        if second_number != 0:
            result = first_number // second_number

        else:
            result = "Error: Cannot perform floor division by zero."

    elif operator == '**':
        result = first_number ** second_number

    else:
        result = "Invalid operator entered."

    print("Result:", result)

except ValueError:
    print("Invalid input. Please enter numeric values only.")
