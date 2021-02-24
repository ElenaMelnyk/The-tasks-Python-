##У програмі генерується випадкове ціле число від 0 до 100.
##Користувач повинен його відгадати не більше ніж за 10 спроб.
##Після кожної невдалої спроби повинно повідомлятися чи більше чи менше
##введене користувачем число, ніж те, що загадане.
##Якщо за 10 спроб число не відгадане, то вивести загадане число.


import random
print ('''The program chooses the number between 1 for 100 and you must guess this number.
You have 10 attempts.''') 
number = random.randint (1,100)
user_number = int (input ("Input the number: "))
attempts = 1

while attempts <= 10 or user_number == number:
    if user_number not in (0,100):
        print ("Error!")
    
    elif user_number == number:
        print ("Bravo!!! The number that was guessed is %4d" %number)
        break
    elif user_number > number:
        print ("Your number is incorrect and is greater.")
    else:
        print ("Your number is incorrect and is less.")
    user_number = int (input ("Input the number: "))
    attempts += 1

    if attempts == 10 and user_number != number:
        print ("Oh... you used all 10 attempts. The number that was guessed is %4d" %number)





       
  



       
