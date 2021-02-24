##Матриця 5x4 заповнюється введенням з клавіатури (крім останніх елементів рядків).
##Програма повинна обчислювати суму введених елементів кожного рядка і записувати її в останній рядок.
##Наприкінці слід вивести отриману матрицю.
##3 5 6 2 8 4 6 2 3 0 5 4 1 5 7 3

str_of_numbers = input ("Input 16th numbers (use the space for separate them): ")
temp = list (str_of_numbers.split ())
print ("The list of numbers:")
print (temp)
list_number = []
for i in range (len (temp)):
    list_number.append (int (temp[i]))

print ()
coln = []
list_number2 = []
x = 0
y = 4
print ("Table:")
for i in range (int (len(list_number)/4)):
    list_number2.append (list_number [x:y])
    x = y
    y += 4
for item in list_number2:
    print (item)

print ()
print ("The sum of numbers in row is: ")
number_row = 1
for item in list_number2:
    c = sum (item , 0)
    item.append (c)
    print ("%d row: %d" %(number_row, c))
    number_row += 1
    
print ()
print ("New table:")
for item in list_number2:
    print (item)

