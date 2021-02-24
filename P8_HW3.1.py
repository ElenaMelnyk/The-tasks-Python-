##Задано символьний рядок. Розробити програму, яка будує і друкує в алфавітному
##порядку множину малих, множину великих латинських  літер, які містяться у
##заданому рядку, і множину цифр, яких немає у рядку.

from random import randint

my_list = [chr (randint (43, 129)) for i in range (50)]
print ("Our list:")
print (my_list)

vowels_lower = []
for item in my_list:
    if 97 <= ord (item) <= 122:
        vowels_lower.append (item)
vowels_lower.sort ()
print ()
print ("The plural with lower case:")
print (tuple (vowels_lower))
    
vowels_upper = []
for item in my_list:
    if 65 <= ord (item) <= 90:
        vowels_upper.append (item)
vowels_upper.sort ()
print ()
print ("The plural with upper case:")
print (tuple (vowels_upper))

print ()    
set_my_list = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
my_list = set (my_list)
set_my_list.difference_update(my_list)
print ("The numbers what isn't in 'Our list':")
print (set_my_list)
