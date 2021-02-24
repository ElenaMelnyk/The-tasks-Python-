## 1. FizzBuzz Interview Question
## Create a function that takes a number as an argument and returns "Fizz", "Buzz" or "FizzBuzz".
## •	If the number is a multiple of 3 the output should be "Fizz".
## •	If the number given is a multiple of 5, the output should be "Buzz".
## •	If the number given is a multiple of both 3 and 5, the output should be "FizzBuzz".
## •	If the number is not a multiple of either 3 or 5, the number should be output on its
##        own as shown in the examples below.
## •	The output should always be a string even if it is not a multiple of 3 or 5
## Examples
## fizz_buzz(3) ➞ "Fizz"
##
## fizz_buzz(5) ➞ "Buzz"
##
## fizz_buzz(15) ➞ "FizzBuzz"
##
## fizz_buzz(4) ➞ "4"

def count_number (self):
    if self.number == 0:
        return str (self.number)
    elif self.number % 3 == 0 and self.number % 5 == 0:
        return "FizzBuzz"
    elif self.number % 3 == 0:
        return "Fizz"
    elif self.number % 5 == 0:
        return "Buzz"
    else:
        return str(self.number)
        
