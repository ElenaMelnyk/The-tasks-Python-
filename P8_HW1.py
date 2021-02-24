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

my_list = []
upper_case = []
lower_case = []
numbers = []
symbols = []

for i in range (ord("!"), ord ("z")+1):
    my_list.append (chr(i))
print ("My list:")
print (my_list)

for i in range (26):
    lower_case.append (my_list.pop())

for i in range (26):
    upper_case.append (my_list.pop(-7))

for i in range (10):
    numbers.append (my_list.pop(-14))

for i in range (len(my_list)):
    symbols.append (my_list.pop())

upper_case = tuple (upper_case)
lower_case = tuple (lower_case)
numbers = tuple (numbers)
symbols = tuple (symbols)
print()
print ("The 1th tuple: ", lower_case, "\n\nThe 2nd tuple", upper_case, "\n\nThe 2nd tuple", upper_case, "\n\nThe 4th tuple: ",symbols)
print()

my_list = [ numbers, lower_case, upper_case, symbols]
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
