##У другому списку зберегти індекси парних елементів першого списку.
##Наприклад, якщо дано список зі значеннями 8, 3, 15, 6, 4, 2, то  другий
##треба заповнити значеннями 1, 4, 5, 6 (або 0, 3, 4, 5 - якщо індексація
##починається з нуля), оскільки саме в цих позиціях першого масиву стоять парні числа.

import random
list1 = []

for item in range (20):
    list1.append (random.randint (0,15))
print ("The first List: ", list1)

list2 = []
for item in range (20):
    if list1[item] % 2 == 0:
        item2 = list1.index (list1[item])
        list2.append (item2)
print ("The second List: ", list2)
