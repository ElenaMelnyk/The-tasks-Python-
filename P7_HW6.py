##Написати функцію is_prime, яка приймає 1 аргумент - число від 0 до 1000,
##і повертає True, якщо воно просте, і False - в іншому випадку.

def is_prime (number):
    list_numbers = []
    for i in range (1000):
        list_numbers.append (i)

    count_divisors = []
    while number in list_numbers:
        for i in range (1, 1000):
            if number % i == 0:
                count_divisors.append (i)
        if len (count_divisors) == 2: return "True"
        else: return "False"
    else: return "False"


                
print ("""The program determines the character of number.
True - natural number
False - another number""")
number = int (input ("Input the number: "))
print ("The answer is: ", is_prime (number))
