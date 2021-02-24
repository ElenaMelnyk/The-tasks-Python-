##Створити список, що містить цифри, літери алфавіту (великі та малі),
##спеціальні символи;
##
##Розділити список на декілька, кожний з яких містить тільки цифри, тільки літери тощо;
##
##Конвертувати списки в кортежі;
##
##Ввести з клавіатури почергово цифру, літеру чи спецсимвол і повернути відповідно
##індекс входження у відповідний кортеж;
##
##Відобразити реверс одного з кортежів.

def result_input (data):
    for i in range (len (my_list)):
        if data in my_list[i]:
            return i, my_list[i].index(data)
from random import randint

my_list = []
upper_case = []
lower_case = []
numbers = []
symbols = []

for i in range(20):
    my_list.append(str(randint(0,9)))

for i in range(20):
    my_list.append(chr(randint(65,90)))

for i in range(20):
    my_list.append(chr(randint(97,122)))

my_list.extend(['!', '@', '#', '$', '%'])

print(my_list)

for item in my_list:
    if item in '0123456789':
        numbers.append(item)
    elif 65 <= ord(item) <= 90:
        upper_case.append(item)
    elif 97 <= ord(item) <= 122:
        lower_case.append(item)
    else:
        symbols.append(item)

upper_case = tuple (upper_case)
lower_case = tuple (lower_case)
numbers = tuple (numbers)
symbols = tuple (symbols)
print()
print ("The 1th tuple: ", lower_case, "\n\nThe 2nd tuple", upper_case, "\n\nThe 2nd tuple", upper_case, "\n\nThe 4th tuple: ",symbols)
print()

my_list = [numbers, lower_case, upper_case, symbols]
print ("My list:")
print (my_list)

data = input ("Input a value: ")
print ("The index of data in List is: ", result_input (data))    

print ()
print (upper_case)
upper_case = list (upper_case)
upper_case.reverse ()
upper_case = tuple (upper_case)
print ()
print (upper_case)
