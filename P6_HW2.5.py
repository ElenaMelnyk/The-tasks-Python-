##Дві матриці заповнюються введенням з клавіатури.
##В елементи третьої матриці такої ж розмірності записати більші з
##відповідних елементів перших двох. 

import random
print ("The count of the number of digits should be multiples of three.")
numbers_first_table = input ("Input numbers: ")
numbers_second_table = input ("Input numbers: ")
row = 3
column = 3
sum_table = []

print ()
table1 = []
str_numbers_first_table = numbers_first_table.split()
for i in range (len (str_numbers_first_table)):
    table1.append (int (str_numbers_first_table [i]))
    sum_table.append (int (str_numbers_first_table [i]))
table2 = []
str_numbers_second_table = numbers_second_table.split()
for i in range (len (str_numbers_second_table)):
    table2.append (int (str_numbers_second_table [i]))
    sum_table.append (int (str_numbers_second_table [i]))
sum_table.sort()


print ("The first table:")
temp = []
y = 0
x = 3
for j in range (int (len (table1)/3)):
    temp.append (table1 [y:x])
    print (table1 [y:x])
    y = x
    x += 3

print ()
print ("The second table:")
temp2 = []
y = 0
x = 3
for j in range (int (len (table1)/3)):
    temp2.append (table1 [y:x])
    print (table2 [y:x])
    y = x
    x += 3

print ()
print ("The third table:")
temp3 = []
y = int (len (sum_table)/2)
x = int (len (sum_table)/2) + 3
for j in range (int (len (sum_table)/6)):
    temp3.append (sum_table [y:x])
    print (sum_table [y:x])
    y = x
    x += 3    

