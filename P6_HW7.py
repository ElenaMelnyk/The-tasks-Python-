##У списку знайти елементи, які в ньому зустрічаються тільки один раз,і вивести їх на екран. 

import random
list1 = []

for item in range (20):
    list1.append (random.randint (0,10))
print ("The first List: ", list1)

list2 = []
for item in range (20):
    if list1.count (list1[item]) == 1:
        list2.append (list1[item])
print ("The first List with unique numbers: ", list2)
