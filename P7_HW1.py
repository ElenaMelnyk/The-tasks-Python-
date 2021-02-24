##Написати функцію arithmetic, яка приймає 3 аргументи: перші 2 - числа,
##третій - операцію, яка повинна бути здійснена над ними.
##Якщо третій аргумент +, додати їх; якщо -, то відняти; * - помножити;
##/ - розділити (перше на друге). В інших випадках повернути рядок "Невідома операція".


def arithmetic (first_number, second_number, operation):
    
    if operation == "+": return first_number + second_number
    if operation == "-": return first_number - second_number
    if operation == "*": return first_number * second_number
    if operation == "/": return first_number / second_number
    else: return "Unknown operation"

first_number = int (input ("Input the number: "))
second_number = int (input ("Input the number: "))
operation = input ("Input the operation - '+', '-', '*', '/': ")
print ("The result is: %.2f" %arithmetic (first_number, second_number, operation)) 
