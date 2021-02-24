##Задано два символьних рядка із малих і великих латинських літер та цифр.
##Розробити програму, яка будує і друкує в алфавітному порядку множину літер,
##які є в обох масивах, і множини літер окремо першого і другого масивів.

from random import randint
row1 = [chr (randint (48,57)) for i in range (15)]
row1.extend (chr (randint (65,90)) for i in range (15))
row1.extend (chr (randint (97,122)) for i in range (15))
print ("The first row: ", row1)
print()
row2 = [chr (randint (48,57)) for i in range (15)]
row2.extend (chr (randint (65,90)) for i in range (15))
row2.extend (chr (randint (97,122)) for i in range (15))
print ("The second row: ", row2)

print ()
row1 = set (row1)
row2 = set (row2)
number = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
row3 = set ()
row1.difference_update (number)
row2.difference_update (number)
result = row3.union (row1, row2)
print ("Update first row: ")
for x in sorted (row1):
    print ("%s " %x, end = '')
print ()
print ("Update second row: ")
for x in sorted (row2):
    print ("%s " %x, end = '')
print ()
print ("Union row:")
for x in sorted (result):
    print ("%s " %x, end = '')
print ()
