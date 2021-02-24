def arithmetic (first_number, second_number, operation):
    
    if operation == "+":
        return first_number + second_number
    elif operation == "-":
        return first_number - second_number
    elif operation == "*":
        return first_number * second_number
    elif operation == "/":
        return first_number / second_number
    else:
        return "Unknown operation"

first_number = int (input ("Input the number: "))
second_number = int (input ("Input the number: "))
operation = input ("Input the operation - '+', '-', '*', '/': ")
print ("The result is: ", arithmetic (first_number, second_number, operation)) 
