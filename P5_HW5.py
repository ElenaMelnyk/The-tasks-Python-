##Дано число P  і число H. Користувач вводить послідовність чисел.
##Визначити: суму тих чисел, які менше P; добуток чисел, які більші за H;
##кількість чисел, що знаходяться  в діапазоні значень від P до H.
##При введенні числа рівного P або H, припинити обчислення та вивести результат.

import random

P = random.randint (1,50)
H = random.randint (1,50)
if P > H:
    P, H = H, P 
sum_numbers = 0
mult_numbers = 1
count_numbers = 0

print ("Number P= ", P)
print ("Number H= ", H)
print ("If you want to stop the program input the number P or H and click 'enter'.")
number = int (input ("Input the number: "))
i = 0
list_num = []
while 1 < 2:
    list_num.append (number)
    print (list_num)
    if number < P:
        sum_numbers += number
    elif number > H:
        mult_numbers *= number
    elif number > P and number < H:
        count_numbers += 1
    elif number == P or number == H:
        break
    print ("Sum of numbers is: ", sum_numbers)
    print ("Multiply of numbers is: ", mult_numbers)
    print ("The count of numbers between the P from H is: ", count_numbers)
    number = int (input ("Input number: "))





