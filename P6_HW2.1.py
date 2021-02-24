##Порахувати суми кожного рядка і кожного стовпця матриці.
##Доповнити її стовпцем, який містить суми елементів рядків та рядком,
##елементами якого є суми елементів стовпців.

import random
from pprint import pprint
row = int (input ("Input the count of the rows: "))
column = int (input("Input the count of the columns: "))

print ()
print ("Table")
table = [] 
for i in range(column):
    coln = [random.randint(10, 20) for j in range(row)]
    table.append(coln)
    print ("%4s" %coln)

print ()
sum_number_row = []
for i in range (column):
    a = 0
    for j in range (row):
        a += table [i][j]
    sum_number_row.append (a)
print ("The sum of the numbers in row:")   
pprint (sum_number_row)        

print ()
sum_number_column = []
for j in range (row):
    a = 0
    for i in range (column):
        a += table [i][j]
    sum_number_column.append (a)
print ("The sum of the numbers in column:")   
pprint (sum_number_column)

print ()
print ("New table with new row: ")
new_table = list (table)
new_table.append (sum_number_row)
for item in new_table:
    print (item)
    
print ()
print ("New table with new column: ")
new_table2 = list (table)
i=0
for item in new_table2:
    item.insert(len (item), sum_number_column[i])
    i +=1
    print (item)

