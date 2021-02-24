##Задано n рядочків символів.  Розробити програму, яка визначає і друкує окремо
##приголосні та голосні малі літери латинського алфавіту, які є в кожному рядку.

from random import randint
my_list = []

vowels = ["a", "e", "i", "o", "u"]
consonants = []

n = int (input ("Input the count of row: "))

for j in range (n):
    row = [chr (randint (97,122)) for i in range (15)]
    my_list.append (row)
    print (row)

for i in range (len (my_list)):
    for j in range (15):
        if my_list[i][j] in vowels:
            print ("%s " %my_list[i][j], end='')
    print ()
for i in range (len (my_list)):
    for j in range (15):
        if my_list[i][j] not in vowels:
            print ("%s " %my_list[i][j], end='')
    print ()
