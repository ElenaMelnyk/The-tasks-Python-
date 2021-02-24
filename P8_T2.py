##Створіть множину із списку: ['boat', 'bus', 'plane', 'train'].

set1 = set (['boat', 'bus', 'plane', 'train'])
print (set1)
print ()

##Створіть множину із кортежу: ('cyclist', 'driver', 'pedestrian').

set2 = set (('cyclist', 'driver', 'pedestrian'))
print (set2)
print ()

##Задано множину символів від 'a' до 'z‘. Скласти програму, яка визначає
##і виводить на екран елементи цієї множини в алфавітному порядку.

x = ord ("a")
y = ord ("z")

alphabet = set ()
for i in range (x, y+1):
    alphabet.add(chr(i))
for j in sorted (alphabet):
    print ("%s, " %j, end = '')
print ()

##Задано текст з цифр і літер латинського алфавіту. Скласти програму,
##яка визначає, яких літер – голосних {a, e, i, o, u, y} або приголосних
##більше в цьому тексті.

print ()
vow = {"a", "e", "i", "o", "u", "y"}
number = set ()

for num in range (48,58):
    number.add (chr(num))

my_string = input ("Input the string: ")
count_v = 0
count_num = 0
count_s = 0
count_k = 0
for symb in my_string:
    if symb in vow:
        count_v += 1
    elif symb in number:
        count_num += 1
    elif symb in ". , : ; ' ! ?":
        count_s += 1
    else:
        count_k += 1

if count_s > count_k:
    print ("More vowels")
else:
    print ("More consonants")
    
print ("The count of vowels %d \nThe count of numbers %d \nThe count of space %d." % (count_v, count_num, count_s))
