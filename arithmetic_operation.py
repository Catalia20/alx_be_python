def perform_operation(num1, num2, oporation):
    if operation == "add":
            return num1 + num2
    elif operation == "subtract":
            return num1 - num2
    elif operation == "multiply":
            return num1 * num2
    elif operation == "divide":
            if num2 == 0:
                print("Sorry, you can not divide by zero")
            else:
                return num1 / num2
    else:
        print("Retry!")
