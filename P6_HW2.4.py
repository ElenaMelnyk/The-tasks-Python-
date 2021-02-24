##Знайти максимальний елемент серед мінімальних елементів стовпців матриці.

import random
row = int (input ("Input the count of the rows: "))
column = int (input("Input the count of the columns: "))

print ()
print ("Table:")
table = []
for i in range (row):
    coln = [random.randint (0,50) for j in range (column)]
    coln = sorted (coln)
    table.append (coln)
    print (coln)

print ()
max_number = 0
for item in table:
    item = sorted (item)
    if max_number < item [0]:
        max_number = item [0]
print ("The number max in the column among numbers min in the rows is: ", max_number)

