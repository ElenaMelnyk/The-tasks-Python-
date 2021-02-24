##Сформувати матрицю з чисел від 0 до 999, вивести її на екран.
##Порахувати кількість двозначних чисел в ній.

import random
row = int (input ("Input the count of the rows: "))
column = int (input("Input the count of the columns: "))
print ()
print ("Table")
table = []
for i in range (column):
    coln = [random.randint (0,150) for j in range (row)]
    table.append (coln)
    print (coln)

print ()
count = 0
for item in table:
    for i in range (column):
        if item [i] < 99 and item [i] >9:
            count += 1
print ("The count of the number of two-digit numbers in Table is: ", count)
