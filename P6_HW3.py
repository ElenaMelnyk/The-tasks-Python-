##Згенерувати 20 випадкових цілих чисел в діапазоні від -5 до 4,
##записати їх в список. Порахувати кількість додатних, від’ємних і нульових елементів.
##Вивести на екран елементи списку і пораховані кількості.

import random
list1 = []

for item in range (20):
    list1.append (random.randint (-5,4))
print ("List: ", list1)
coun_item_zero = 0
count_item_positive = 0
count_item_negative = 0
for item in range (20):
    if list1[item] == 0:
        coun_item_zero += 1
    elif list1[item] < 0:
        count_item_positive += 1
    else:
        count_item_negative += 1
print ("The count of numbers equal zero is: ", coun_item_zero)
print ("The count of positive numbers is: ", count_item_positive)
print ("The count of negative numbers is: ", count_item_negative)
