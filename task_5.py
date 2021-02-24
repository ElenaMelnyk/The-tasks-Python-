##5. List of Multiples
##Create a function that takes two numbers as arguments (num, length) and
##returns a list of multiples of num up to length.

def list_of_multiples (num, length):
    my_list = [num * i for i in range (1,length+1) ]
    return my_list
    
num = int (input ("Input first number "))
length = int (input ("Input second number "))
list_of_multiples (num, length)
