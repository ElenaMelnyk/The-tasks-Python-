##Заповнити список випадковими додатними і від’ємними цілими числами.
##Вивести його на екран. Видалити з списку всі від’ємні елементи і знову вивести.

import random
list1 = []

for item in range (20):
    list1.append (random.randint (-10,10))
print ("The List: ", list1)

for item in range (20):
    if list1[item] < 0:
        list1[item] = "x"
        
list2 = []
for item in range (20):
    if list1[item] != "x":
        list2.append(list1[item])
print ("The list without negative numbers: ", list2)
