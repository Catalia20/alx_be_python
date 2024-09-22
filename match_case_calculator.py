# alx_be_python
Directory: control-flow
File: match_case_calculator.py

num1 = float(input("Enter the first number:1"))
num2 = float(input("Enter the second number:2"))
operation = input("choose the operation (+,-,*,/):")
match operation:
    case '+':
        result = num1 + num2
        print(f"The result is {result}.")
    case '-':
        result = num1 - num2
        print(f"The result is {result}.")
    case '*':
        result = num1 * num2
        print(f"The result is {result}.")
    case '/':
        if num2 != 0:
            result = num1 / num2
            print(f"The result is {result}.")
            else:
                print("cannot divide by zero.")
                case _:
                    print("Invalid operation.Please choose one of +,-,*,/.")
                    
            

 
