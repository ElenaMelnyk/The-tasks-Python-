##У масиві випадкових цілих чисел поміняти місцями мінімальний і максимальний елементи.


import random

countNumbers = 20
numbers = []
print ("First list")
for i in range (countNumbers):
    numbers.append (random.randint(1,100))
    print ("%d, " %numbers[i], end = "")

print ()
print ("Second list")
minNum = min(numbers)
maxNum = max(numbers)

temp = numbers[numbers.index(minNum)]
numbers[numbers.index(minNum)] = numbers[numbers.index(maxNum)]
numbers[numbers.index(maxNum)] = temp

for i in numbers:
    print ("%d, " %i, end = "")
