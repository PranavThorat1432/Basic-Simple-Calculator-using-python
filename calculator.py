# Basic Simple Calculator

# Function for performing calculations
def calculator():
    while True:  # Loop to keep the calculator running

        # Variables for taking input
        num1 = float(input("Enter Num 1: "))  
        num2 = float(input("Enter Num 2: "))
        operation = input("Enter an operand (+,-,*,/) or 'q' to quit: ")

        # Condition for quitting the calculator
        if operation == 'q':
            print("Quitting the Calculator!\n")
            break  # Exit the loop

        # Condition if the operand is invalid
        if operation not in ['+','-','*','/']:
            print("Invalid Operand. Please select from (+,-,*,/)")
            continue  

        # Perform the selected operation
        if operation == '+':  # Execute if input is +

            print(num1, operation, num2, "=", num1 + num2)  # Perform addition

        elif operation == '-':  # Execute if input is -

            print(num1, operation, num2, "=", num1 - num2)  # Perform subtraction

        elif operation == '*':  # Execute if input is *

            print(num1, operation, num2, "=", num1 * num2)  # Perform multiplication
            
        elif operation == '/':  # Execute if input is /

            if num2 != 0:  # Check if the divisor is not zero
                print(num1, operation, num2, "=", num1 / num2)  # Perform division
            else:  
                print("Error: Division by zero.\n")

        else:
            print("Invalid Operator! Please select from (+,-,*,/)")

calculator()  # Call the function to start the calculator
