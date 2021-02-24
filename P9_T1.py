##Створіть словник, в якому ключі – це числа, а значення – їх рядкова
##інтерпретація. Напишіть програму, що перетворює цей словник, в якому
##ключами будуть рядки а значеннями - числа.

my_dictionary = {}
my_dictionary [1] = "one"
my_dictionary [2] = "two"
my_dictionary [3] = "three"
my_dictionary [4] = "four"

print ("The old dictionary: ", my_dictionary)
print ()
for i in range (1,5):
    my_dictionary [my_dictionary [i]] = i
    my_dictionary.pop (i)
print ("The new dictionary: ", my_dictionary)
