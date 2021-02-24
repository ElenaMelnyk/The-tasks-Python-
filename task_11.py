## 11. Is the Number a Repdigit
## A repdigit is a positive number composed out of the same digit.
## Create a function that takes an integer and returns whether it's a repdigit
## or not.

def repdigit (number):
    if number < 0:
        return print ("False")
    elif number == 0:
        return print ("True")
    else:
        str_number = str(number)
        list_number = list(str_number)
        count_number = list_number.count(list_number[0])
        if count_number == len (list_number):
            return print("True")
        else:
            return print ("False")
        


number = int (input ("Input the number: "))
print ("Is the number repdigit?")
repdigit (number)
