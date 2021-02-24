##Задано символьний рядок. Розробити програму, яка вилучає з цього рядка
##всі повторні входження цифр і знаків арифметичних операцій.

from random import randint
my_list = [chr (randint (60, 123)) for i in range (50)]
print ("The list: ",my_list)

set_list = set (my_list)
print ("The list without duplicate: ", set_list)
